package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.media.Image;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    TextView mainTxt;
    Button mainBtn;
    Button dButton;
    Button reset;
    ImageButton imageButton;
    private long score = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mainTxt = findViewById(R.id.mainTxt);
        mainBtn = findViewById(R.id.main_btn);
        dButton =  findViewById(R.id.d_button);
        reset = findViewById(R.id.reset_button);
        imageButton = findViewById(R.id.imageButton);


        //обработчик события нажатия на кнопку увеличения
        View.OnClickListener clickListener = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                score ++;
                String s;
                if(score%10==2 || score%10==3 || score%10==4){
                    s = String.format("Кнопка нажата %s раза",score);
                }
                else{
                    s = String.format("Кнопка нажата %s раз",score);
                }
                mainTxt.setText(s.toCharArray(),0, s.length());
            }
        };
        //обработчик события нажатия на кнопку уменьшения
        View.OnClickListener clickListener2 = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                score --;
                String s;
                if(score%10==2 || score%10==3 || score%10==4){
                    s = String.format("Кнопка нажата %s раза",score);
                }
                else{
                    s = String.format("Кнопка нажата %s раз",score);
                }
                mainTxt.setText(s.toCharArray(),0, s.length());
            }
        };
        //обработчик события нажатия на сброс
        View.OnClickListener clickListener3 = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                score = 0;
                String s = "Кнопка нажата 0 раз";
                mainTxt.setText(s.toCharArray(),0, s.length());
            }
        };

        mainBtn.setOnClickListener(clickListener);
        dButton.setOnClickListener(clickListener2);
        reset.setOnClickListener(clickListener3);
        imageButton.setOnClickListener(clickListener3);
    }

}