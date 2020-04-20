//Globals
const today = new Date();
const date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
var IDMAKER = 0;

//Data class
class weatherElement {
    constructor(d, t, te, sc, h, p, l) {
        this.date = "Data: " + d;
        this.time = "Time: " + t;
        this.temp = "Temp: " + Number((te - 273.15) * 9 / 5 + 32).toFixed(1) + "\xB0" + "F"; //Fahrenheit
        this.skyConditions = "Sky Conditions: " + sc; //clear, cloudy, snowy, etc.
        this.humidity = "Humidity: " + h + " %";//%
        this.pressure = "Pressure: " + p / 1000 + " kPa";//kPa
        this.likelyhood = l;
    }
}

//helper functions
var test = function () {
    console.log("TestComplete");
}
var idmaker = function () {
    IDMAKER++;
    return IDMAKER;
}
var cycle = function (w) {
    console.log(w);
    if (w == "likely") {
        w = "unlikely";
    } else {
        w = "likely";
    }
    console.log(w)
}

//Vue apps
var weather = new Vue({
    el: "#weatherApp",
    data: {
        loaded: false,
        position: {},
        weather: {},
        weatherSnapshotData: [],
        voteCount: {
            default: 0,
            likely: 0,
            unlikely: 0
        }
    },
    beforeCreate: async function () {
        const IP = await getIP();
        console.log(IP)
        this.position = await getCoordinates(IP);
        this.weather = await getCurrentWeather(this.position);
        this.weatherSnapshotData = await getForecast(this.position);
        this.cycle();
        this.loaded = true;
    },
    updated: async function () {
    },
    methods: {
        test: function (i) {
            console.log(i)
        },
        cycle: function () {
            this.voteCount.default = 0;
            this.voteCount.likely = 0;
            this.voteCount.unlikely = 0;
            this.weatherSnapshotData.forEach(e => {
                console.log(e.likelyhood)
                if (e.likelyhood == "likely") {
                    this.voteCount.likely++;
                } else if (e.likelyhood == "unlikely") {
                    this.voteCount.unlikely++;
                } else {
                    this.voteCount.default++;
                }
            });
        }
    }
});

//api functions
function getIP() {
    return fetch('http://api.ipstack.com/check?access_key=56c3d93c938f7b10baf003c5b09dbdf4')
        .then(res => res.json())
        .then(p => { return p.ip })
        .catch(error => console.log(error));
}

function getCoordinates(IP) {
    return fetch("http://api.ipstack.com/" + IP + "?access_key=56c3d93c938f7b10baf003c5b09dbdf4&format=1")
        .then(res => res.json())
        .then(posts => {
            return {
                country: posts.country_code,
                state: posts.region_name,
                city: posts.city,
                lat: posts.latitude,
                long: posts.longitude
            };
        })
        .catch(error => console.log(error));
}

function getCurrentWeather(position) {
    return fetch('http://api.openweathermap.org/data/2.5/weather?lat=' + position.lat + '&lon=' + position.long + "&appid=82598d0499d389c3317c37b28fd53f99")
        .then(res => res.json())
        .then(p => {
            return (new weatherElement(date, time, p.main.temp, p.weather[0].description, p.main.humidity, p.main.pressure));
        })
        .catch(error => console.log(error));
}

function getForecast(position, vueData) {
    return fetch("https://api.openweathermap.org/data/2.5/forecast?lat=" + position.lat + "&lon=" + position.long + "&appid=82598d0499d389c3317c37b28fd53f99")
        .then(res => res.json())
        .then(posts => {
            weatherSnapshotData = [];
            posts.list.forEach(el => {
                let dateTime = el.dt_txt.split(' ');
                let forcastElement = (new weatherElement(dateTime[0], dateTime[1], el.main.temp, el.weather[0].description, el.main.humidity, el.main.pressure))
                weatherSnapshotData.push(forcastElement);
            });
            return weatherSnapshotData;
        })
        .catch(error => console.error("Error: getForcast" + error))
}