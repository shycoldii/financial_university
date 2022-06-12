package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;

public class MessagesActivity extends AppCompatActivity {
    TextView textView;

    /**
     * Инициализирует кнопки/текстовые представления.
     */
    private void initState() {
        textView = findViewById(R.id.textViewMessages);
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
                Intent i = new Intent(  MessagesActivity.this,MainActivity.class);
                startActivity(i);
                break;
            case R.id.friends:
                i = new Intent(  MessagesActivity.this,FriendsActivity.class);
                startActivity(i);
                break;
            case R.id.scroll:
                i = new Intent(  MessagesActivity.this,ScrollActivity.class);
                startActivity(i);
                break;
        }
        return super.onOptionsItemSelected(item);
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_messages);
    }
}