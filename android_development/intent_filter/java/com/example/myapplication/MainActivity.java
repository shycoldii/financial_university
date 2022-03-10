package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.net.Uri;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    Button btnTime;
    Button btnName;
    Button btnDate;
    Button btnAl;
    EditText editText;
    Button btnUrl;
    EditText editUrl;
    TextView tvName;
    TextView colorTest;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btnDate = findViewById(R.id.btnDate);
        btnTime = findViewById(R.id.btnTime);
        editText = findViewById(R.id.etLName);
        tvName = findViewById(R.id.tvName);
        btnName = findViewById(R.id.btnName);
        btnUrl = findViewById(R.id.btnURL);
        editUrl = findViewById(R.id.etLURL);
        colorTest = findViewById(R.id.colorTest);
        btnAl = findViewById(R.id.btnAl);


        View.OnClickListener listener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent;
                switch(view.getId()) {
                    case R.id.btnTime:
                        intent = new Intent("com.example.intent.action.showtime");
                        intent.putExtra("lname", editText.getText().toString());
                        startActivity(intent);
                        break;
                    case R.id.btnDate:
                        intent = new Intent("ru.startandroid.intent.action.showdate");
                        intent.putExtra("lname", editText.getText().toString());
                        startActivity(intent);
                        break;
                    case R.id.btnName:
                        intent = new Intent(getApplicationContext(), NameActivity.class);
                        startActivityForResult(intent, 1);
                        break;
                    case R.id.btnAl:
                        intent = new Intent(getApplicationContext(), AlignmentActivity.class);
                        startActivityForResult(intent, 1);
                        break;
                }

            }
        };
        btnTime.setOnClickListener(listener);
        btnDate.setOnClickListener(listener);
        btnName.setOnClickListener(listener);
        btnAl.setOnClickListener(listener);
        //URL
        btnUrl.setOnClickListener(view -> {
            Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://developer.android.com"));
            startActivity(intent);
        });
        //sys action
        WifiManager wifiManager = (WifiManager)this.getApplicationContext().getSystemService(Context.WIFI_SERVICE);
        if(wifiManager.isWifiEnabled()){
            System.out.println("ENABLED");
        }
        else{
            System.out.println("NOT ENABLED");
        }
    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (data == null) {
            return;
        }
        String name = data.getStringExtra("name");
        String color = data.getStringExtra("color");
        String al = data.getStringExtra("al");
        tvName.setText("Your name is " + name);
        try{
            colorTest.setTextSize(Integer.parseInt(al));
        }
        catch(NumberFormatException|NullPointerException n){
            n.printStackTrace();
        }
        try{
            colorTest.setTextColor(Color.parseColor(color));
        }
        catch(Exception n){
            n.printStackTrace();
            System.out.println("что-то еще не установлено");
        }


    }


}