package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;

public class ScrollActivity extends AppCompatActivity {
    TextView textView;

    /**
     * Инициализирует кнопки/текстовые представления.
     */
    private void initState() {
        textView = findViewById(R.id.textViewScroll);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.main_menu, menu);
        return true;
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        switch(id){
            case R.id.main:
                Intent i = new Intent(  ScrollActivity.this,MainActivity.class);
                startActivity(i);
                break;
            case R.id.friends:
                i = new Intent(  ScrollActivity.this,FriendsActivity.class);
                startActivity(i);
                break;
            case R.id.messages:
                i = new Intent(  ScrollActivity.this,MessagesActivity.class);
                startActivity(i);
                break;
        }
        return super.onOptionsItemSelected(item);
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_scroll);
        initState();
    }
}