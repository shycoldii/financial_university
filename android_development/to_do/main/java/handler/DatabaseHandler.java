package handler;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

import model.Task;

/**
 * Обработчик, работающий с таблицами из базы данных приложения.
 */
public class DatabaseHandler extends SQLiteOpenHelper {
    private final SQLiteDatabase db;

    private static final String TABLE_NAME = "task";
    private static final String DATABASE_NAME = "taskDb";
    private static final int version = 1;
    private static final String CREATE_TABLE_COMMAND =
            "CREATE TABLE " + TABLE_NAME + "( id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                    "name VARCHAR(8000), is_done BOOLEAN, creation_time text, order_number INTEGER)";

    /**
     * Конструктор.
     * @param context - контекст приложения
     */
    public DatabaseHandler(Context context) {
        super(context, DATABASE_NAME, null, version);
        this.db = this.getWritableDatabase();
    }

    @Override
    public void onCreate(SQLiteDatabase sqLiteDatabase) {
        sqLiteDatabase.execSQL(CREATE_TABLE_COMMAND);
    }

    @Override
    public void onUpgrade(SQLiteDatabase sqLiteDatabase, int i, int i1) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_NAME);
        onCreate(db);
    }

    /**
     * Добавляет новую строку сущности "Задача".
     * @param task - задача
     */
    public void insert(Task task){
        ContentValues cv = new ContentValues();
        cv.put("name", task.getName());
        cv.put("is_done", false);
        cv.put("order_number",task.getOrderNumber());
        cv.put("creation_time", task.getCreationTime().toString());
        db.insert(TABLE_NAME, null, cv);
    }

    /**
     * Получает все задачи.
     * @return список задач
     */
    public List<Task> getAll(){
        List<Task> taskList = new ArrayList<>();
        Cursor cur = null;
        db.beginTransaction();

        try{
            cur = db.query(TABLE_NAME, null, null, null, null, null, null, null);
            if(cur != null){
                if(cur.moveToFirst()){
                    do{
                        Task task = new Task(cur.getString(cur.getColumnIndexOrThrow("name")),
                                      cur.getInt(cur.getColumnIndexOrThrow("is_done"))==1,
                                             LocalDateTime.parse(
                                                     cur.getString(cur.getColumnIndexOrThrow("creation_time"))));
                        task.setId(cur.getInt(cur.getColumnIndexOrThrow("id")));
                        task.setOrderNumber(cur.getInt(cur.getColumnIndexOrThrow("order_number")));
                        taskList.add(task);
                    }
                    while(cur.moveToNext());
                }
            }
        }
        finally {
            db.endTransaction();
            assert cur != null;
            cur.close();
        }
        return taskList;
    }

    /**
     * Обновляет значение статуса задачи.
     * @param id - идентификатор задачи.
     * @param isDone - новый статус выполнения задачи.
     */
    public void updateStatus(int id, boolean isDone){
        ContentValues cv = new ContentValues();
        cv.put("is_done", isDone);
        db.update(TABLE_NAME, cv, "id" + "= ?", new String[] {String.valueOf(id)});
    }

    /**
     * Обновляет значение порядкового номера задачи.
     * @param id - идентификатор задачи.
     * @param orderNumber - порядковый номер.
     */
    public void updateOrderNumber(int id, int orderNumber){
        ContentValues cv = new ContentValues();
        cv.put("order_number", orderNumber);
        db.update(TABLE_NAME, cv, "id" + "= ?", new String[] {String.valueOf(id)});
    }

    /**
     * Обновляет содержимое задачи.
     * @param id - идентификатор задачи.
     * @param name - наименование задачи.
     */
    public void updateTask(int id, String name) {
        ContentValues cv = new ContentValues();
        cv.put("name",name);
        db.update(TABLE_NAME, cv, "id" + "= ?", new String[] {String.valueOf(id)});
    }

    /**
     * Удаляет задачу.
     * @param id - идентификатор задачи.
     */
    public void deleteTask(int id){
        db.delete(TABLE_NAME, "id" + "= ?", new String[] {String.valueOf(id)});
    }
}
