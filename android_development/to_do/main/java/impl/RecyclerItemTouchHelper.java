package impl;

import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.graphics.drawable.Drawable;
import android.view.View;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.ItemTouchHelper;
import androidx.recyclerview.widget.RecyclerView;

import com.example.myapplication.R;

import adapter.TaskAdapter;

public class RecyclerItemTouchHelper extends ItemTouchHelper.SimpleCallback {

    /**
     * Адаптер задач.
     */
    private final TaskAdapter taskAdapter;

    /**
     * Конструктор.
     * @param taskAdapter - адаптер задач.
     */
    public RecyclerItemTouchHelper(TaskAdapter taskAdapter) {
        super(ItemTouchHelper.UP | ItemTouchHelper.DOWN, ItemTouchHelper.LEFT | ItemTouchHelper.RIGHT);
        this.taskAdapter = taskAdapter;
    }

    @Override
    public boolean onMove(@NonNull RecyclerView recyclerView, @NonNull RecyclerView.ViewHolder viewHolder, @NonNull RecyclerView.ViewHolder target) {
        taskAdapter.onTaskMove(viewHolder.getAdapterPosition(), target.getAdapterPosition());
        return true;
    }

    @Override
    public void onSwiped(@NonNull RecyclerView.ViewHolder viewHolder, int direction) {
        final int position = viewHolder.getAdapterPosition();
        if (direction == ItemTouchHelper.LEFT) {
            AlertDialog.Builder builder = new AlertDialog.Builder(taskAdapter.getContext());
            builder.setTitle(taskAdapter.getContext().getString(R.string.delete_task));
            builder.setMessage(taskAdapter.getContext().getString(R.string.are_you_sure));
            builder.setPositiveButton(taskAdapter.getContext().getString(R.string.confirm),
                    (dialog, which) -> taskAdapter.deleteTask(position));
            builder.setNegativeButton(R.string.cancel, (dialog, which) -> taskAdapter.notifyItemChanged(viewHolder.getAdapterPosition()));
            AlertDialog dialog = builder.create();
            dialog.show();
        }
        else if (direction == ItemTouchHelper.RIGHT){
          taskAdapter.editTask(position);
        }
    }

    @Override
    public void onChildDraw(@NonNull Canvas c, @NonNull RecyclerView recyclerView, @NonNull RecyclerView.ViewHolder viewHolder, float dX, float dY, int actionState, boolean isCurrentlyActive) {
        super.onChildDraw(c, recyclerView, viewHolder, dX, dY, actionState, isCurrentlyActive);

        Drawable icon;
        ColorDrawable background;

        View itemView = viewHolder.itemView;
        int backgroundCornerOffset = 20;

        //задаем внешний вид
        if (dX > 0) {
            //сдвиг вправо (изменение)
            icon = ContextCompat.getDrawable(taskAdapter.getContext(), R.drawable.ic_baseline_edit);
            background = new ColorDrawable(ContextCompat.getColor(taskAdapter.getContext(), R.color.dark_grey));
        } else {
            //сдвиг влево (удаление)
            icon = ContextCompat.getDrawable(taskAdapter.getContext(), R.drawable.ic_baseline_delete);
            background = new ColorDrawable(Color.parseColor("#b30000"));
        }
        assert icon != null;

        int iconMargin = (itemView.getHeight() - icon.getIntrinsicHeight()) / 2;
        int iconTop = itemView.getTop() + (itemView.getHeight() - icon.getIntrinsicHeight()) / 2;
        int iconBottom = iconTop + icon.getIntrinsicHeight();

        //задаем границы отображения
        if (dX > 0) { // сдвиг вправо (изменение)
            int iconLeft = itemView.getLeft() + iconMargin;
            int iconRight = itemView.getLeft() + iconMargin + icon.getIntrinsicWidth();
            icon.setBounds(iconLeft, iconTop, iconRight, iconBottom);
            background.setBounds(itemView.getLeft(), itemView.getTop(),
                    itemView.getLeft() + ((int) dX) + backgroundCornerOffset, itemView.getBottom());
        } else if (dX < 0) { // сдвиг влево (удаление)
            int iconLeft = itemView.getRight() - iconMargin - icon.getIntrinsicWidth();
            int iconRight = itemView.getRight() - iconMargin;
            icon.setBounds(iconLeft, iconTop, iconRight, iconBottom);
            background.setBounds(itemView.getRight() + ((int) dX) - backgroundCornerOffset,
                    itemView.getTop(), itemView.getRight(), itemView.getBottom());
        } else { // не тронут
            background.setBounds(0, 0, 0, 0);
        }
        background.draw(c);
        icon.draw(c);
    }
}
