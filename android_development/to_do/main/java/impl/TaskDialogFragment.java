package impl;

import android.app.Activity;
import android.content.DialogInterface;
import android.graphics.Color;
import android.os.Build;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.annotation.RequiresApi;
import androidx.core.content.ContextCompat;

import com.example.myapplication.DialogCloseInterface;
import com.example.myapplication.R;
import com.google.android.material.bottomsheet.BottomSheetDialogFragment;

import java.time.LocalDateTime;
import java.util.Comparator;
import java.util.Objects;
import java.util.Optional;
import java.util.OptionalInt;
import java.util.stream.IntStream;

import handler.DatabaseHandler;
import model.Task;

/**
 * Модальная нижняя таблица добавления/изменения задачи.
 * Имеет свой ЖЦ.
 */
public class TaskDialogFragment extends BottomSheetDialogFragment {
    public static final String TAG = "TaskDialogFragment";

    private EditText newTaskText;
    private Button newTaskSaveButton;
    private DatabaseHandler dbHandler;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.new_task_layout, container, false);
        Objects.requireNonNull(getDialog()).getWindow().setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_ADJUST_RESIZE);
        return view;
    }

    @RequiresApi(api = Build.VERSION_CODES.N)
    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        boolean isUpdate = false;
        newTaskText = requireView().findViewById(R.id.newTaskText);
        newTaskSaveButton = requireView().findViewById(R.id.newTaskButton);
        dbHandler = new DatabaseHandler(getActivity());

        final Bundle bundle = getArguments();
        if(bundle != null){
            isUpdate = true;
            updateViewItems(bundle);
        }
        newTaskText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }
            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                if(s.toString().isEmpty()){
                    newTaskSaveButton.setEnabled(false);
                    newTaskSaveButton.setTextColor(Color.parseColor("#b30000"));
                }
                else{
                    newTaskSaveButton.setEnabled(true);
                    newTaskSaveButton.setTextColor(ContextCompat.getColor(requireContext(),R.color.dark_grey));
                }
            }
            @Override
            public void afterTextChanged(Editable s) {
            }
        });

        boolean isUpdateFinal = isUpdate;

        newTaskSaveButton.setOnClickListener(v -> {
            String text = newTaskText.getText().toString();
            if(isUpdateFinal){
                dbHandler.updateTask(bundle.getInt("id"), text);
            }
            else {
                if(!text.isEmpty()){
                    Task task = new Task(text,false, LocalDateTime.now());
                    OptionalInt maxNumber = dbHandler.getAll().stream().mapToInt(Task::getOrderNumber).max();
                    if(maxNumber.isPresent()){
                        task.setOrderNumber(maxNumber.getAsInt()+1);
                    }
                    else{
                        task.setOrderNumber(1);
                    }
                    dbHandler.insert(task);
                }
            }
            dismiss();
        });
    }

    @Override
    public void onDismiss(@NonNull DialogInterface dialog){
        Activity activity = getActivity();
        if(activity instanceof DialogCloseInterface)
            ((DialogCloseInterface)activity).handleDialogClose(dialog);
    }

    /**
     * Обновляет состояние текстовых представлений.
     * Т.е. при открытии окна на изменение задачи подтянется ее состояние.
     * @param bundle - бандл.
     */
    private void updateViewItems(Bundle bundle){
        String name = bundle.getString("name");
        newTaskText.setText(name);
        assert name != null;
        if(name.length()>0)
            newTaskSaveButton.setTextColor(ContextCompat.getColor(requireContext(), R.color.dark_grey));
    }

}
