package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.SeekBar;
import android.widget.TextView;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class MainActivity extends AppCompatActivity {
    private TextView txtView;
    private Button button;
    private EditText editText;
    private Integer number;
    private SeekBar seekBar;
    private int hardLevel = 0;
    private final Map<Integer,Integer> boundaries = new HashMap<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initState();
        generateNumber();
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(button.getText().toString().equals(getString(R.string.play_more))){
                    resetGame();
                }
                else if (!editTextIsEmpty()){
                   try{
                       int userNumber = Integer.parseInt(editText.getText().toString());
                       int maxValue = boundaries.get(hardLevel);
                       if(userNumber>(maxValue) || userNumber<1){
                           txtView.setText(R.string.error);
                       }
                       else if(userNumber<number) txtView.setText(R.string.behind);
                       else if(userNumber>number) txtView.setText(R.string.ahead);
                       else{
                           //кейс: юзер отгадал число
                           generateNumber();
                           txtView.setText(R.string.hit);
                           button.setText(R.string.play_more);
                       }
                   }
                   catch (NumberFormatException n){
                        txtView.setText(R.string.error);
                   }
                }
            }
        });
        seekBar.setOnSeekBarChangeListener(seekBarChangeListener);
    }

    /**
     * Управление уровнем сложности юзера.
     */
    private final SeekBar.OnSeekBarChangeListener seekBarChangeListener = new SeekBar.OnSeekBarChangeListener() {
        @Override
        public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
            if(hardLevel!=progress){
                hardLevel = progress;
                resetGame();
                generateNumber();
            }
        }

        @Override
        public void onStartTrackingTouch(SeekBar seekBar) {

        }

        @Override
        public void onStopTrackingTouch(SeekBar seekBar) {

        }
    };

    /**
     * Инициализирует кнопки/текстовые представления.
     */
    private void initState() {
        button = findViewById(R.id.button);
        txtView = findViewById(R.id.txtView);
        editText = findViewById(R.id.editText);
        seekBar = findViewById(R.id.seekBar);
        boundaries.put(0,101);
        boundaries.put(1,1001);
        boundaries.put(2,10001);
    }

    /**
     * Сбросить настройки игры.
     */
    private void resetGame(){
        button.setText(R.string.input_value);
        editText.setText("");
        switch(hardLevel){
            case 0:
                txtView.setText(R.string.try_to_guess_easy);
                break;
            case 1:
                txtView.setText(R.string.try_to_guess_normal);
                break;
            case 2:
                txtView.setText(R.string.try_to_guess_hard);
                break;
        }
    }

    /**
     * Генерирует рандомное число по уровню сложности.
     */
    private void generateNumber() {
        number = 1+ new Random().nextInt(boundaries.get(hardLevel));

    }
    /**
     * Проверяет, что ввел пользователь.
     */
    private boolean editTextIsEmpty() {
        return editText.getText().toString().isEmpty();
    }

}