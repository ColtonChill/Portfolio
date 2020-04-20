import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        TaskQueue queue = new TaskQueue();
        ResultTable results = new ResultTable();
        ArrayList<Thread> threadArray = new ArrayList<>();
        int start = (int)System.currentTimeMillis();
        for(int i=0; i<Runtime.getRuntime().availableProcessors();++i){
            Thread t = new Thread(new WorkerThread(queue, results));
            threadArray.add(t);
            t.start();
        }
        for(int i=0;i<threadArray.size();++i) {
            threadArray.get(i).join();
        }
        results.display();
        int time = ((int)System.currentTimeMillis()-start);
        System.out.println("\nPi Computation took: "+time+"ms");

    }
}
