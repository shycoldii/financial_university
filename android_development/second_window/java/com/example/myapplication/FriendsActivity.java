package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;

public class FriendsActivity extends AppCompatActivity {
    TextView textView;
    TextView friendView;

    /**
     * Инициализирует кнопки/текстовые представления.
     */
    private void initState() {
        friendView = findViewById(R.id.newFriends);
        textView = findViewById(R.id.textView1);
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
                Intent i = new Intent(  FriendsActivity.this,MainActivity.class);
                startActivity(i);
                break;
            case R.id.scroll:
                i = new Intent(  FriendsActivity.this,ScrollActivity.class);
                startActivity(i);
                break;
            case R.id.messages:
                i = new Intent(  FriendsActivity.this,MessagesActivity.class);
                startActivity(i);
                break;
        }
        return super.onOptionsItemSelected(item);
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.acitivity_friends);
        initState();
        Bundle arguments = getIntent().getExtras();
        if(arguments!=null){
            Object name = arguments.get("friend");
            if(name!=null){
                friendView.setText(name.toString());
            }
        }
    }

}