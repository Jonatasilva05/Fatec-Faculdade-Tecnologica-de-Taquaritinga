-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 26, 2024 at 08:37 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `serenus`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `data_cadastro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `nome`, `username`, `email`, `senha`, `data_cadastro`) VALUES
(1, 'jhon', 'jonatas', 'jonatasmoraes05@gmail.com', '$2y$10$TmHv2S0svnluX0j9I.qOR.8F1kg.vJ.599MWoYRI52EwQUCsnPySa', '2024-11-13 18:28:44'),
(2, 'jonatas', 'jhon', 'jonatasmoraes016@gmail.com', '$2y$10$YjEw0obybfFhrPioGuxxu.DfhEiSbmGH5lHXlbXWFGkkdxoaaAHlG', '2024-11-13 18:34:19'),
(3, 'davi', 'davi', 'teste@gmail.com', '$2y$10$za3tDqo.s8rkdZqoK24ikucEG1VArj7XbXhLjk/Q2C9z/pX3sCFEu', '2024-11-13 20:01:19'),
(4, 'gost', 'gost', 'gost@gmail.com', '$2y$10$p3NIC2kFhBsxkhyCJozNheGkMSYJvFBnxcHYb8kS0rDaX1hI5zwU2', '2024-11-14 02:52:56'),
(5, 'teste', 'teste', 'testea@gmail.com', '$2y$10$VB7EozrCIMRyopq8P7s7YOyC2OVhbnvYxuRbBewh34prpMXymPEnG', '2024-11-14 02:55:30'),
(6, 'Jonatas', 'jhonSilva', 'jonatasmoraes0805@gmail.com', '$2y$10$DhJIj01PJmBdrda.JtiQiuMdBjO.yZR4wR5Zmd7Kopjp7kE8m8Mzi', '2024-11-26 16:59:26'),
(7, 'Fabiana', 'faby', 'fabi@gmail.com', '$2y$10$u6QJkeupZHz2WFkANWc6iO2JPsUmULm/jP/elKEWt24LCFefLNG7W', '2024-11-26 17:03:18');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
