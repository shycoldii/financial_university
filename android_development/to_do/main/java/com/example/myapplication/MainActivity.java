package com.example.myapplication;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.ItemTouchHelper;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.annotation.SuppressLint;
import android.content.DialogInterface;
import android.os.Build;
import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.util.Objects;

import adapter.TaskAdapter;
import handler.DatabaseHandler;
import impl.RecyclerItemTouchHelper;
import impl.TaskDialogFragment;

/**
 * Основная активность приложения.
 */
public class MainActivity extends AppCompatActivity implements DialogCloseInterface {

    private TaskAdapter taskAdapter;
    private DatabaseHandler dbHandler;

    @RequiresApi(api = Build.VERSION_CODES.N)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //убираем сверху
        Objects.requireNonNull(getSupportActionBar()).hide();
        initState();
    }

    /**
     * Инициализирует приложение.
     */
    @RequiresApi(api = Build.VERSION_CODES.N)
    private void initState(){
        dbHandler = new DatabaseHandler(getApplicationContext());

        RecyclerView taskRecyclerView = findViewById(R.id.tasksRecyclerView);
        taskRecyclerView.setLayoutManager(new LinearLayoutManager(this));
        FloatingActionButton fab = findViewById(R.id.fab);
        fab.setOnClickListener(v ->
                new TaskDialogFragment().show(getSupportFragmentManager(), TaskDialogFragment.TAG));

        taskAdapter = new TaskAdapter(dbHandler,MainActivity.this);
        taskRecyclerView.setAdapter(taskAdapter);
        prepareTasks();

        ItemTouchHelper itemTouchHelper = new ItemTouchHelper(new RecyclerItemTouchHelper(taskAdapter));
        itemTouchHelper.attachToRecyclerView(taskRecyclerView);
    }

    @SuppressLint("NotifyDataSetChanged")
    @RequiresApi(api = Build.VERSION_CODES.N)
    @Override
    public void handleDialogClose(DialogInterface dialogInterface) {
        //актуализация полученной информации
        prepareTasks();
        taskAdapter.notifyDataSetChanged();
    }

    /**
     * Подгатавливает задачи к отображению.
     * (Берутся из БД) при запуске приложения.
     */
    @RequiresApi(api = Build.VERSION_CODES.N)
    private void prepareTasks(){
        taskAdapter.setTasks(dbHandler.getAll());
        taskAdapter.sortTasksByOrder();
    }
}