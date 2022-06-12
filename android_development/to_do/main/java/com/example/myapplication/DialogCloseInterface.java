package com.example.myapplication;

import android.content.DialogInterface;

/**
 * Интерфейс для реализации логики при закрытии диалогового окна.
 */
public interface DialogCloseInterface {

    /**
     * Реализует логику закрытия диалового окна.
     * @param dialogInterface - интерфейс диалога
     */
    void handleDialogClose(DialogInterface dialogInterface);
}
