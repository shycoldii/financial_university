package adapter;

import android.annotation.SuppressLint;
import android.content.Context;
import android.os.Build;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.CompoundButton;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.recyclerview.widget.RecyclerView;

import com.example.myapplication.MainActivity;
import com.example.myapplication.R;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

import handler.DatabaseHandler;
import impl.TaskDialogFragment;
import model.Task;

/**
 * Адаптер списка задач.
 */
public class TaskAdapter extends RecyclerView.Adapter<TaskAdapter.ViewHolder> {

    private List<Task> tasks = new ArrayList<>();
    private final MainActivity activity;
    private final DatabaseHandler dbHandler;

    /**
     * Конструктор.
     * @param dbHandler - обработчик БД.
     * @param activity - основная активность.
     */
    public TaskAdapter(DatabaseHandler dbHandler, MainActivity activity) {
        this.activity = activity;
        this.dbHandler = dbHandler;
    }

    /**
     * Получить контекст приложения.
     * @return контекст.
     */
    public Context getContext() {
        return activity;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        //создает новый объект ViewHolder всякий раз, когда RecyclerView нуждается в этом
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.task_layout, parent, false);
        return new ViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(@NonNull TaskAdapter.ViewHolder holder, int position) {
        final Task task = tasks.get(position);
        holder.checkBox.setText(task.getName());
        holder.checkBox.setChecked(task.getDone());
        holder.checkBox.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                dbHandler.updateStatus(task.getId(), b);
                task.setDone(b);
            }
        });
    }

    @Override
    public int getItemCount() {
        return tasks.size();
    }

    /**
     * Устанавливает значение списку задач.
     * @param tasks - список задач.
     */
    public void setTasks(List<Task> tasks) {
        this.tasks = tasks;
    }

    /**
     * Класс отображения задач.
     */
    public static class ViewHolder extends RecyclerView.ViewHolder {
        CheckBox checkBox;

        ViewHolder(View view) {
            super(view);
            checkBox = view.findViewById(R.id.todoCheckBox);
        }
    }

    /**
     * Изменить содержимое задачи. Вызывается при "сдвиге" пользователем вправо.
     * @param position - позиция задачи в списке.
     */
    public void editTask(int position) {
        Task task = tasks.get(position);
        Bundle bundle = new Bundle();
        bundle.putInt("id", task.getId());
        bundle.putString("name", task.getName());
        TaskDialogFragment fragment = new TaskDialogFragment();
        fragment.setArguments(bundle);
        fragment.show(activity.getSupportFragmentManager(), TaskDialogFragment.TAG);
    }

    /**
     * Удалить содержимое задачи. Вызывается при "сдвиге" пользователем влево.
     * @param position - позиция задачи в списке.
     */
    @RequiresApi(api = Build.VERSION_CODES.N)
    public void deleteTask(int position) {
        Task task = tasks.get(position);
        for(int i = 0; i<position; i++){
            dbHandler.updateOrderNumber(tasks.get(i).getId(),
                    tasks.get(i).getOrderNumber()-1);
        }
        dbHandler.deleteTask(task.getId());
        retrieveTasks();
    }

    /**
     * Изменяет положение задачи при перемещении.
     * @param startPos - начальная позиция
     * @param endPos - конечная позиция
     */
    @RequiresApi(api = Build.VERSION_CODES.N)
    public void onTaskMove(int startPos, int endPos){

        Task fromTask = tasks.get(startPos);
        Task toTask  = tasks.get(endPos);
        dbHandler.updateOrderNumber(fromTask.getId(),toTask.getOrderNumber());
        dbHandler.updateOrderNumber(toTask.getId(),fromTask.getOrderNumber());
        retrieveTasks();
    }

    /**
     * Сортирует задачи по порядковому номеру.
     */
    @RequiresApi(api = Build.VERSION_CODES.N)
    public void sortTasksByOrder(){
        tasks.sort(Comparator.comparingInt(Task::getOrderNumber).reversed());
    }

    /**
     * Сортирует задачи по дате создания (сначала новые).
     */
    @RequiresApi(api = Build.VERSION_CODES.N)
    public void sortTasksByDateAsc(){
       //todo
    }

    /**
     * Сортирует задачи по дате создания (сначала старые).
     */
    @RequiresApi(api = Build.VERSION_CODES.N)
    public void sortTasksByDateDesc(){
        //todo
    }

    /**
     * Изменяет порядковые номера задач в соответствии с сортировкой
     * дат.
     */
    public void OnTaskSortByDate(){
         //todo
    }

    /**
     * Получает список задач из БД.
     * Используется после проведения операций.
     * Сортирует список.
     * Оповещает адаптер.
     */
    @SuppressLint("NotifyDataSetChanged")
    @RequiresApi(api = Build.VERSION_CODES.N)
    public void retrieveTasks(){
        tasks = dbHandler.getAll();
        this.notifyDataSetChanged();
        sortTasksByOrder();
    }


}
