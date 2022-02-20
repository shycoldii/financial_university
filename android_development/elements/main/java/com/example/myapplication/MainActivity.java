package com.example.myapplication;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Comparator;

public class MainActivity extends AppCompatActivity {
    Button button;
    Button ok_btn, cnc_btn;
    EditText editText;
    TextView textView;
    ListView mainListView;
    ArrayAdapter<String> mArrayAdapter;
    ArrayList<String> mNameList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initState();
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!editText.getText().toString().isEmpty()){
                    textView.setText(String.format(getString(R.string.hello),
                            editText.getText().toString()));
                    String value = editText.getText().toString();
                    if (!mNameList.contains(value)){
                        mNameList.add(editText.getText().toString());
                        mNameList.sort(Comparator.comparing(String::toLowerCase));
                    }
                    mArrayAdapter.notifyDataSetChanged();
                }

            }
        });
        mainListView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                //textView.setText(String.format(getString(R.string.hello),
                //        mNameList.get(i).toString()));
                AlertDialog.Builder adb=new AlertDialog.Builder(MainActivity.this);
                adb.setTitle("Delete?");
                adb.setMessage("Are you sure you want to delete " + mNameList.get(i));
                final int positionToRemove = i;
                adb.setNegativeButton("Cancel", null);
                adb.setPositiveButton("Ok", new AlertDialog.OnClickListener() {
                    public void onClick(DialogInterface dialog, int which) {
                        mNameList.remove(positionToRemove);
                        mArrayAdapter.notifyDataSetChanged();
                    }});
                adb.show();
            }});
        View.OnClickListener oclBtn = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // по id определеяем кнопку, вызвавшую этот обработчик
                switch (v.getId()) {
                    case R.id.ok_btn:
                        // кнопка ОК
                        Toast.makeText(getApplicationContext(), getString(R.string.ok), Toast.LENGTH_LONG).show();
                        textView.setText(getString(R.string.ok));
                        break;
                    case R.id.cnc_btn:
                        // кнопка Cancel
                        Toast.makeText(getApplicationContext(), getString(R.string.cancel), Toast.LENGTH_LONG).show();
                        textView.setText(getString(R.string.cancel));
                        break;
                }
            }
        };
        ok_btn.setOnClickListener(oclBtn);
        cnc_btn.setOnClickListener(oclBtn);
    }

    /**
     * Инициализирует состояние.
     */
    private void initState(){
        textView = findViewById(R.id.txtView);
        ok_btn = findViewById(R.id.ok_btn);
        cnc_btn = findViewById(R.id.cnc_btn);
        mainListView = findViewById(R.id.main_listview);
        mArrayAdapter = new ArrayAdapter<>(this,
                android.R.layout.simple_list_item_1,
                mNameList);
        mainListView.setAdapter(mArrayAdapter);
        button = findViewById(R.id.buttonUpdate);
        editText = findViewById(R.id.editTextTextPersonName2);
        textView.setText(String.format(getString(R.string.hello),getString(R.string.name)));
    }
}