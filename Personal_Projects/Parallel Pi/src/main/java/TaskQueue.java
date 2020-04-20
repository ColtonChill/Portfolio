import java.util.ArrayList;
import java.util.LinkedList;
import static java.util.Collections.shuffle;

public class TaskQueue {
    private LinkedList<Integer> queue = new LinkedList<Integer>();
    TaskQueue(int n){
        //make process and populate the queue, 1000, 1 per digit to compute
        this.populate(n);
    }
    TaskQueue(){
        this.populate(1000);
    }

    private void populate(int n){
         ArrayList<Integer> jobIDs= new ArrayList<>();
         for(int i =0; i<n;++i){
             jobIDs.add(i);
         }
         shuffle(jobIDs);
         for (int i =0; i<n; ++i){
            queue.add(jobIDs.get(i));
         }
    }
    public synchronized int pop(){
        return (queue.pop());
    }
    public boolean empty(){
        return queue.isEmpty();
    }
}

