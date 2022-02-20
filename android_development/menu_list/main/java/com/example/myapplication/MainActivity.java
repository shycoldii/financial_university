package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.CheckBox;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    // Элементы экрана
    TextView tv;
    CheckBox chb;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // находим элементы
        tv = findViewById(R.id.textView);
        chb = findViewById(R.id.chbExtMenu);

    }

    // создание меню
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // добавляем пункты меню
        getMenuInflater().inflate(R.menu.mymenu, menu);
        return super.onCreateOptionsMenu(menu);
    }
    // обновление меню
    @Override
    public boolean onPrepareOptionsMenu(Menu menu) {
        // пункты меню с ID группы = 1 видны,
        // если в CheckBox стоит галка
        menu.setGroupVisible(R.id.group1, chb.isChecked());
        return super.onPrepareOptionsMenu(menu);
    }
    // обработка нажатий
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        StringBuilder sb = new StringBuilder();
        // Выведем в TextView информацию о нажатом пункте меню
        sb.append("Item Menu");
        sb.append("\r\n groupId: " + item.getGroupId());
        sb.append("\r\n itemId: " + item.getItemId());
        sb.append("\r\n order: " + item.getOrder());
        sb.append("\r\n title: " + item.getTitle());
        tv.setText(sb.toString());
        if(getString(R.string.exit).equals(item.getTitle().toString())){
            this.finish();
        }

        return super.onOptionsItemSelected(item);
    }


}
