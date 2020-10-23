-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Май 01 2020 г., 20:00
-- Версия сервера: 5.6.38
-- Версия PHP: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `Firma`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Nomenclatura`
--

CREATE TABLE `Nomenclatura` (
  `id` int(11) NOT NULL,
  `tovar` varchar(30) NOT NULL,
  `idScl` int(11) NOT NULL,
  `Col` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Nomenclatura`
--

INSERT INTO `Nomenclatura` (`id`, `tovar`, `idScl`, `Col`) VALUES
(1, 'Стол', 1, 10),
(1, 'Стол', 0, 0),
(1, 'Стул', 2, 10),
(0, 'Даша', 1, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `Scladi`
--

CREATE TABLE `Scladi` (
  `id` int(11) NOT NULL,
  `naz` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Scladi`
--

INSERT INTO `Scladi` (`id`, `naz`) VALUES
(1, 'Основной'),
(2, 'Розничный');

-- --------------------------------------------------------

--
-- Структура таблицы `USERS`
--

CREATE TABLE `USERS` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `pass` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `USERS`
--

INSERT INTO `USERS` (`id`, `name`, `pass`) VALUES
(1, 'Иванов О.В.', '827ccb0eea8a706c4c34a16891f84e7b'),
(2, 'Петров М.П.', 'b5434fd1f943d03206ad17e54d9442a6');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `USERS`
--
ALTER TABLE `USERS`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `USERS`
--
ALTER TABLE `USERS`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
