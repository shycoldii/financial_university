package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

public class AlignmentActivity extends AppCompatActivity {
    Button btnOnk;
    EditText editTextAl;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_alignment);
        editTextAl = findViewById(R.id.editTextAl);
        btnOnk = findViewById(R.id.btnOKA);
        btnOnk.setOnClickListener(view -> {
            Intent intent = new Intent();
            intent.putExtra("al",editTextAl.getText().toString());
            setResult(RESULT_OK, intent);
            finish();
        });
    }
}