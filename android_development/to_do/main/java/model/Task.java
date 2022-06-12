package model;

import java.time.LocalDateTime;

/**
 * Сущность "Задача".
 */
public class Task {

    private int id;
    private Boolean isDone;
    private String name;
    private LocalDateTime creationTime;
    private Integer orderNumber;

    /**
     * Конструктор.
     * @param name - наименование
     * @param isDone - статус выполнения
     */
    public Task(String name, Boolean isDone, LocalDateTime creationTime){
        this.isDone = isDone;
        this.name = name;
        this.creationTime = creationTime;
    }

    /**
     * Устанавливает значение идентификатору.
     * @param id - идентификатор.
     */
    public void setId(int id) {
        this.id = id;
    }

    /**
     * Устанавливает значение наименованию задачи.
     * @param name - наименование.
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Получает значение идентификатора.
     * @return id - идентификатор.
     */
    public int getId() {
        return id;
    }

    /**
     * Получает статус выполнения задачи.
     * @return isDone - статус выполнения задачи.
     */
    public Boolean getDone() {
        return isDone;
    }

    /**
     * Получает значение наименования.
     * @return name - наименование.
     */
    public String getName() {
        return name;
    }

    /**
     * Получает значение времени создания.
     * @return creationTime - время создания сущности.
     */
    public LocalDateTime getCreationTime() {
        return creationTime;
    }

    /**
     * Получает порядковое значение задачи.
     * @return orderNumber - порядковое значение задачи.
     */
    public Integer getOrderNumber() {
        return orderNumber;
    }

    /**
     * Устанавливает порядковое значение задачи.
     */
    public void setOrderNumber(Integer orderNumber) {
        this.orderNumber = orderNumber;
    }

    /**
     * Устанавливает статус выполнения.
     * @param done - выполнено/нет
     */
    public void setDone(Boolean done) {
        isDone = done;
    }
}
