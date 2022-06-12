package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class NameActivity extends AppCompatActivity {
    EditText editText;
    TextView textView;
    Button btnOnk;
    EditText editTextColor;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_name);
        editText = findViewById(R.id.etName);
        editTextColor = findViewById(R.id.editTextColor);
        textView = findViewById(R.id.textView1);
        btnOnk = findViewById(R.id.btnOK);
        btnOnk.setOnClickListener(view -> {
            Intent intent = new Intent();
            intent.putExtra("name", editText.getText().toString());
            intent.putExtra("color",editTextColor.getText().toString());
            setResult(RESULT_OK, intent);
            finish();
        });
    }
}