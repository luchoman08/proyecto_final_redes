-- phpMyAdmin SQL Dump
-- version 4.0.10.12
-- http://www.phpmyadmin.net
--
-- Servidor: 127.7.106.131:3306
-- Tiempo de generación: 01-03-2016 a las 09:57:31
-- Versión del servidor: 5.5.45
-- Versión de PHP: 5.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `mypythonapp`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cpu_usage`
--

CREATE TABLE IF NOT EXISTS `cpu_usage` (
  `fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `us` int(11) DEFAULT NULL,
  `sy` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  `wa` int(11) DEFAULT NULL,
  `st` int(11) DEFAULT NULL,
  PRIMARY KEY (`fecha`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mem_usage`
--

CREATE TABLE IF NOT EXISTS `mem_usage` (
  `fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `swpd` int(11) DEFAULT NULL,
  `free` int(11) DEFAULT NULL,
  `buff` int(11) DEFAULT NULL,
  `cache` int(11) DEFAULT NULL,
  PRIMARY KEY (`fecha`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `os`
--

CREATE TABLE IF NOT EXISTS `os` (
  `fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `kernel` varchar(50) DEFAULT NULL,
  `rel` varchar(50) DEFAULT NULL,
  `nodename` varchar(50) DEFAULT NULL,
  `kernelversion` varchar(50) DEFAULT NULL,
  `machine` varchar(50) DEFAULT NULL,
  `processor` varchar(50) DEFAULT NULL,
  `operatingsystem` varchar(50) DEFAULT NULL,
  `hardware` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fecha`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Estructura de tabla para la tabla `swap_usage`
--

CREATE TABLE IF NOT EXISTS `swap_usage` (
  `fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `si` int(11) DEFAULT NULL,
  `so` int(11) DEFAULT NULL,
  PRIMARY KEY (`fecha`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fecha`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
