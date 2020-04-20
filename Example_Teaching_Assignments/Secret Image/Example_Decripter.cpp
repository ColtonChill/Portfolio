#include <iostream>
#include <fstream>
#include <string>
using namespace std;
											//Colton Hill 
void correction(int&, int&, char,int&);

int main() {
	ofstream fout;
	ifstream fin;
	//fin.open("3.ppm");
	//fout.open("o.ppm");
	string header, dFile, cFile;
	int color, Color, c=0;
	char d = 't';

	cout << "Welcome to the Portable Pixmap (PPM) Image Decoder!\n"
		<< "Please enter the name of distorted image file (Extension included): \n";
	cin >> dFile;
	fin.open(dFile);
	if (!fin) {
		while (!fin) {
			cout << "\nThis file failed to open. Please retype the file or check that it is in the right location.\n";
			cin >> dFile;
			fin.open(dFile);
		}
	}
	cout << "Please enter the name of corrected image file: \n";
	cin >> cFile;
	fout.open(cFile);
	while (!fout) {
		cout << "\nThis file failed to open. Please retype the file or check that it is in the right location.\n";
		cin >> cFile;
		fout.open(cFile);
	}
	cout << "Please enter the distortion method (b=Bronze, s=Silver, g=Gold):\n";
	cin >> d;
	while (d != 'b' && d != 's' && d != 'g') {
		cout << "I dont know that destortion method\n"
			<< "Please enter b (Bronze), s (Silver) or g (Gold): ";
		cin >> d;
	}
	cout << "Please wait...\n\n";
	

	for (int i = 0; i < 3; i++) {
		getline(fin, header);
		fout << header<<endl;
	}

	while (fin >> color) {
		correction(c,color,d,Color);
		fout << color << " ";
	}
	cout << cFile <<" created." << endl;
	fin.close();
	fout.close();
	return 0;
}
void correction(int & c, int & color, char type, int & Color) {
	if (type == 'b') {
		if (c == 0) {
			color *= 10;
			c++;
		}else if (c == 1) {
			color = 0;
			c++;
		}else if (c == 2) {
			color = 0;
			c = 0;
		}
	}else if (type == 's') {
		if (c == 0) {
			color = 0;
			c++;
		}
		else if (c == 1) {
			color *= 20;
			c++;
		}
		else if (c == 2) {
			color *= 20;
			c = 0;
		}
	}
	else if (type == 'g') {
		if (c == 0) {
			Color = color;
			color /= 1000000;
			c++;
		}
		else if (c == 1) {
			color = (Color % 1000000)/1000;
			c++;
		}
		else if (c == 2) {
			color =(Color%1000);
			c = 0;
		}
	}
}