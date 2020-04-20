import java.util.HashMap;

public class ResultTable {
    private HashMap<Integer, Integer> table = new HashMap<Integer, Integer>();
    public synchronized void add(int index, int n){
        table.put(index,n);
    }
    public void display(){
        System.out.println();
        System.out.print("3.");
        for (int i = 0; i < 1000; ++i) {
            System.out.print(table.get(i));
        }
    }
    public synchronized void printPeriod(){
        if(this.table.size()%10 == 0){
            System.out.print(".");
        }
        if(this.table.size()%250==0){
            System.out.println();
        }
        System.out.flush();
    }
}
