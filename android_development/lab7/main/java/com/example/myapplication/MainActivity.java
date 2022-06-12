package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    TextView textView;
    Button button;
    EditText editText;
    final String TAG = "States";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Log.d(TAG, "MainActivity: onCreate()");
        initState();
        button.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                if(!editText.getText().toString().isEmpty()){
                    Intent i = new Intent(  MainActivity.this,FriendsActivity.class);
                    i.putExtra("friend", editText.getText().toString());
                    startActivity(i);
                }
            }
        });
    }

    /**
     * Инициализирует кнопки/текстовые представления.
     */
    private void initState() {
        textView = findViewById(R.id.txtView1);
        editText =findViewById(R.id.editTextTextPersonName);
        button = findViewById(R.id.button);
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
            case R.id.friends:
                Intent i = new Intent( MainActivity.this, FriendsActivity.class);
                startActivity(i);
                break;
            case R.id.scroll:
                i = new Intent(  MainActivity.this,ScrollActivity.class);
                startActivity(i);
                break;
            case R.id.messages:
                i = new Intent(  MainActivity.this,MessagesActivity.class);
                startActivity(i);
                break;
        }
        return super.onOptionsItemSelected(item);
    }

    @Override
    protected void onStart() {
        super.onStart();
        Log.d(TAG, "MainActivity: onStart()");
    }
    @Override
    protected void onResume() {
        super.onResume();
        Log.d(TAG, "MainActivity: onResume()");
    }
    @Override
    protected void onPause() {
        super.onPause();
        Log.d(TAG, "MainActivity: onPause()");
    }
    @Override
    protected void onStop() {
        super.onStop();
        Log.d(TAG, "MainActivity: onStop()");
    }
    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d(TAG, "MainActivity: onDestroy()");
    }
    @Override
    protected void onRestart() {
        super.onRestart();
        Log.d(TAG, "MainActivity: onRestart()");
    }


}