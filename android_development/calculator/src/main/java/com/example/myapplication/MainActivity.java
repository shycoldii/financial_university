package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.TypedValue;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private Button button1;
    private Button button2;
    private Button button3;
    private Button button4;
    private Button button5;
    private Button button6;
    private Button button7;
    private Button button8;
    private Button button9;
    private Button button0;
    private Button buttonDot;
    private Button buttonSub;
    private Button buttonPercentage;
    private Button buttonMultiply;
    private Button buttonEq;
    private Button buttonDiv;
    private Button buttonAdd;
    private Button buttonReset;
    private Button buttonSign;
    private TextView textView;
    private Double value1 = Double.NaN;
    private Double value2 = Double.NaN;
    private final String DIV = "/";
    private final String MULT = "*";
    private final String SUB = "-";
    private final String ADD = "+";
    private String ACTION = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initButtons();
        //Добавление слушателей на кнопки
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isError()) return;
                checkActionBefore();
                checkReset();
                updateLength();
                StringBuilder result = new StringBuilder();
                result.append(textView.getText().toString())
                        .append("1");
                if (textView.getText().toString().length() <= 33 & !textView.getText().equals(getString(R.string.error)))
                    textView.setText(result);
                checkActionAfter();
            }
        });
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isError()) return;
                checkActionBefore();
                checkReset();
                updateLength();
                StringBuilder result = new StringBuilder();
                result.append(textView.getText().toString())
                        .append("2");
                if (textView.getText().toString().length() <= 33 & !isError())
                    textView.setText(result);
                checkActionAfter();
            }
        });
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isError()) return;
                checkActionBefore();
                checkReset();
                updateLength();
                StringBuilder result = new StringBuilder();
                result.append(textView.getText().toString())
                        .append("3");
                if (textView.getText().toString().length() <= 33 & !isError())
                    textView.setText(result);
                checkActionAfter();
            }
        });
        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (textView.getText().equals(getString(R.string.error))) return;
                checkActionBefore();
                checkReset();
                updateLength();
                StringBuilder result = new StringBuilder();
                result.append(textView.getText().toString())
                        .append("4");
                if (textView.getText().toString().length() <= 33 & !isError())
                    textView.setText(result);
                checkActionAfter();
            }
        });
        button5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (textView.getText().equals(getString(R.string.error))) return;
                checkActionBefore();
                checkReset();
                updateLength();
                StringBuilder result = new StringBuilder();
                result.append(textView.getText().toString())
                        .append("5");
                if (textView.getText().toString().length() <= 33 & !isError())
                    textView.setText(result);
                checkActionAfter();
            }
        });
        button6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (textView.getText().equals(getString(R.string.error))) return;
                checkActionBefore();
                checkReset();
                updateLength();
                StringBuilder result = new StringBuilder();
                result.append(textView.getText().toString())
                        .append("6");
                if (textView.getText().toString().length() <= 33 & !isError())
                    textView.setText(result);
                checkActionAfter();
            }
        });
        button7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (textView.getText().equals(getString(R.string.error))) return;
                checkActionBefore();
                checkReset();
                updateLength();
                StringBuilder result = new StringBuilder();
                result.append(textView.getText().toString())
                        .append("7");
                if (textView.getText().toString().length() <= 33 & !isError())
                    textView.setText(result);
                checkActionAfter();
            }
        });
        button8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (textView.getText().equals(getString(R.string.error))) return;
                checkActionBefore();
                checkReset();
                updateLength();
                StringBuilder result = new StringBuilder();
                result.append(textView.getText().toString())
                        .append("8");
                if (textView.getText().toString().length() <= 33 & !isError())
                    textView.setText(result);
                checkActionAfter();
            }
        });
        button9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (textView.getText().equals(getString(R.string.error))) return;
                checkActionBefore();
                checkReset();
                updateLength();
                StringBuilder result = new StringBuilder();
                result.append(textView.getText().toString())
                        .append("9");
                if (textView.getText().toString().length() <= 33 & !isError())
                    textView.setText(result);
                checkActionAfter();
            }
        });
        button0.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isError()) return;
                checkActionBefore();
                checkReset();
                updateLength();
                StringBuilder result = new StringBuilder();
                result.append(textView.getText().toString())
                        .append("0");
                if (textView.getText().toString().length() <= 33 & !isError())
                    textView.setText(result);
                checkActionAfter();
            }
        });
        buttonDot.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isError()) return;
                checkActionBefore();
                checkReset();
                updateLength();
                StringBuilder result = new StringBuilder();
                result.append(textView.getText().toString().equals("") ?
                        getString(R.string._0) :
                        textView.getText().toString())
                        .append(".");
                if (textView.getText().toString().length() <= 33 & !isError())
                    textView.setText(result);
                checkActionAfter();
            }
        });
        buttonReset.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                value1 = Double.NaN;
                value2 = Double.NaN;
                ACTION = "";
                textView.setText(R.string._0);
                buttonReset.setText(R.string.reset);
                updateLength();
            }
        });
        buttonSign.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isError()) return;
                value1 = Double.parseDouble(textView.getText().toString());
                if (value1 < 0) {
                    textView.setText(textView.getText().toString().substring(1));
                } else if (value1 > 0) {
                    StringBuilder result = new StringBuilder();
                    result.append("-").append(textView.getText().toString());
                    textView.setText(result);
                }
                updateLength();
            }
        });
        buttonPercentage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isError()) return;
                value1 = Double.parseDouble(textView.getText().toString());
                value1 /= 100;
                if (textView.getText().toString().length() <= 33)
                    textView.setText(String.valueOf(value1));
                updateLength();
            }
        });
        buttonDiv.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isError()) return;
                updateRes();
                updateLength();
                ACTION = DIV;
            }
        });
        buttonMultiply.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isError()) return;
                updateRes();
                updateLength();
                ACTION = MULT;
            }
        });
        buttonAdd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isError()) return;
                updateRes();
                updateLength();
                ACTION = ADD;
            }
        });
        buttonSub.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isError()) return;
                updateRes();
                updateLength();
                ACTION = SUB;
            }
        });
        buttonEq.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isError()) return;
                updateRes();
                updateLength();
            }
        });
    }

    /**
     * Проверяет, ошибка ли выведена.
     *
     * @return true, если ошибка.
     */
    private boolean isError() {
        return textView.getText().equals(getString(R.string.error));
    }

    /**
     * Очищает поле ввода при действиях.
     */
    private void checkActionBefore() {
        if (!ACTION.isEmpty() & value2.isNaN() & !isError()) {
            value1 = Double.parseDouble(textView.getText().toString());
            textView.setText("");
            value2 = value1;
        }
    }

    /**
     * Устанавливает значение второму множителю.
     */
    private void checkActionAfter() {
        if (!ACTION.isEmpty()) {
            value2 = Double.parseDouble(textView.getText().toString());
        }
    }

    /**
     * Обновляет результат при операции.
     */
    private void updateRes() {
        if (!value2.isNaN()) {
            if (!isError()) {
                value1 = getResult();
                ACTION = "";
                value2 = Double.NaN;
                if (!isError())
                    if (checkDouble(value1))
                        textView.setText(String.valueOf(value1.intValue()));
                    else textView.setText(String.valueOf(value1));
            }
        }
    }

    /**
     * Проверяет, можно ли представить число в integer.
     *
     * @param result - число для проверки
     * @return true, если можно
     */
    private boolean checkDouble(Double result) {
        return result.intValue() == result;
    }

    /**
     * Получает результат в зависимости от операции.
     *
     * @return result
     */
    private Double getResult() {
        switch (ACTION) {
            case DIV:
                Double result = value1 / value2;
                if (result.isInfinite()) {
                    textView.setText(R.string.error);
                    return Double.NaN;
                }
                return result;


            case MULT:
                return value1 * value2;
            case ADD:
                return value1 + value2;
            case SUB:
                return value1 - value2;
        }
        return Double.NaN;
    }

    /**
     * Уменьшает размер текста, если больше 10 символов.
     */
    private void updateLength() {
        if (textView.getText().toString().length() > 9) {
            textView.setTextSize(TypedValue.COMPLEX_UNIT_SP, 40);
        } else {
            System.out.println(textView.getTextSize());
            textView.setTextSize(TypedValue.COMPLEX_UNIT_SP, 70);
        }
    }

    /**
     * Если поле ввода/вывода непустое, то AC -> C.
     * Если равен 0, то пустота.
     */
    private void checkReset() {
        if (!textView.getText().toString().isEmpty()) {
            buttonReset.setText(R.string.reset_2);
        }
        if (textView.getText().equals("0")) {
            textView.setText("");
        }
    }

    /**
     * Инициализирует кнопки/текстовые представления.
     */
    private void initButtons() {
        button1 = findViewById(R.id.button1);
        button2 = findViewById(R.id.button2);
        button3 = findViewById(R.id.button3);
        button4 = findViewById(R.id.button4);
        button5 = findViewById(R.id.button5);
        button6 = findViewById(R.id.button6);
        button7 = findViewById(R.id.button7);
        button8 = findViewById(R.id.button8);
        button9 = findViewById(R.id.button9);
        button0 = findViewById(R.id.button0);
        buttonDot = findViewById(R.id.button_dot);
        textView = findViewById(R.id.text_view);
        buttonEq = findViewById(R.id.button_equal);
        buttonMultiply = findViewById(R.id.button_multi);
        buttonDiv = findViewById(R.id.button_divide);
        buttonAdd = findViewById(R.id.button_add);
        buttonSub = findViewById(R.id.button_sub);
        buttonReset = findViewById(R.id.button_reset);
        buttonPercentage = findViewById(R.id.button_percentage);
        buttonSign = findViewById(R.id.button_sign);
    }
}