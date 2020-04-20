class WorkerThread implements Runnable{
    private TaskQueue taskQueue;
    private ResultTable resultTable;
    public WorkerThread(TaskQueue t, ResultTable r){
        this.taskQueue = t;
        this.resultTable = r;
    }
    @Override
    public void run() {
        while(!taskQueue.empty()) {
            int key = this.taskQueue.pop();
            this.resultTable.add(key, new Bpp().getDecimal(key+1));
            this.resultTable.printPeriod();
        }
    }
}
