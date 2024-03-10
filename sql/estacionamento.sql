-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 10-Mar-2024 às 00:58
-- Versão do servidor: 10.4.27-MariaDB
-- versão do PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bd`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `estacionamento`
--

CREATE TABLE `estacionamento` (
  `idEstacionamento` int(11) NOT NULL,
  `nomeFantasia` varchar(45) DEFAULT NULL,
  `DtultRelatorio` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `CNPJ` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `estacionamento`
--

INSERT INTO `estacionamento` (`idEstacionamento`, `nomeFantasia`, `DtultRelatorio`, `CNPJ`) VALUES
(1, 'PG PARK', '0000-00-00 00:00:00', 0),
(2, 'PARCO', '0000-00-00 00:00:00', 0),
(3, 'EST. MINEIRÃO', '0000-00-00 00:00:00', 0),
(4, 'PARK MIL', '0000-00-00 00:00:00', 0),
(5, 'TOTAL PARK', '0000-00-00 00:00:00', 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `estacionamento`
--
ALTER TABLE `estacionamento`
  ADD PRIMARY KEY (`idEstacionamento`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `estacionamento`
--
ALTER TABLE `estacionamento`
  MODIFY `idEstacionamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
