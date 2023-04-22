CREATE DATABASE  IF NOT EXISTS `turnero` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `turnero`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: turnero
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrador`
--

DROP TABLE IF EXISTS `administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador` (
  `id_Administrador` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Apellido` varchar(45) NOT NULL,
  `DNI` int NOT NULL,
  `Cargo` varchar(45) NOT NULL,
  `Telefono` int NOT NULL,
  `Email` varchar(45) NOT NULL,
  PRIMARY KEY (`id_Administrador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador`
--

LOCK TABLES `administrador` WRITE;
/*!40000 ALTER TABLE `administrador` DISABLE KEYS */;
/*!40000 ALTER TABLE `administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `especialista`
--

DROP TABLE IF EXISTS `especialista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `especialista` (
  `idEspecialista` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `dni` varchar(45) NOT NULL,
  `nroMatricula` varchar(45) NOT NULL,
  `especialidad` varchar(45) NOT NULL,
  `telefono` int NOT NULL,
  `email` varchar(45) NOT NULL,
  `horarioAtencion` time NOT NULL,
  `Administrador_id_Administrador` int NOT NULL,
  PRIMARY KEY (`idEspecialista`),
  KEY `fk_Especialista_Administrador_idx` (`Administrador_id_Administrador`),
  CONSTRAINT `fk_Especialista_Administrador` FOREIGN KEY (`Administrador_id_Administrador`) REFERENCES `administrador` (`id_Administrador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especialista`
--

LOCK TABLES `especialista` WRITE;
/*!40000 ALTER TABLE `especialista` DISABLE KEYS */;
/*!40000 ALTER TABLE `especialista` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `horarioespecialista`
--

DROP TABLE IF EXISTS `horarioespecialista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horarioespecialista` (
  `id_horarioEspecialista` int NOT NULL AUTO_INCREMENT,
  `diaSemana` varchar(45) NOT NULL,
  `horarInicio` time NOT NULL,
  `horaFin` time NOT NULL,
  `Especialista_idEspecialista` int NOT NULL,
  PRIMARY KEY (`id_horarioEspecialista`),
  KEY `fk_horarioEspecialista_Especialista1_idx` (`Especialista_idEspecialista`),
  CONSTRAINT `fk_horarioEspecialista_Especialista1` FOREIGN KEY (`Especialista_idEspecialista`) REFERENCES `especialista` (`idEspecialista`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horarioespecialista`
--

LOCK TABLES `horarioespecialista` WRITE;
/*!40000 ALTER TABLE `horarioespecialista` DISABLE KEYS */;
/*!40000 ALTER TABLE `horarioespecialista` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `obrasocial`
--

DROP TABLE IF EXISTS `obrasocial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `obrasocial` (
  `id_ObraSocial` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `plan` varchar(45) NOT NULL,
  `nroAfiliados` int NOT NULL,
  `Paciente_idPaciente` int NOT NULL,
  PRIMARY KEY (`id_ObraSocial`,`Paciente_idPaciente`),
  KEY `fk_ObraSocial_Paciente1_idx` (`Paciente_idPaciente`),
  CONSTRAINT `fk_ObraSocial_Paciente1` FOREIGN KEY (`Paciente_idPaciente`) REFERENCES `paciente` (`idPaciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `obrasocial`
--

LOCK TABLES `obrasocial` WRITE;
/*!40000 ALTER TABLE `obrasocial` DISABLE KEYS */;
/*!40000 ALTER TABLE `obrasocial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paciente`
--

DROP TABLE IF EXISTS `paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paciente` (
  `idPaciente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `DNI` int NOT NULL,
  `nroAfiliado` int NOT NULL,
  `telefono` int NOT NULL,
  `email` varchar(45) NOT NULL,
  `Administrador_id_Administrador` int NOT NULL,
  PRIMARY KEY (`idPaciente`),
  KEY `fk_Paciente_Administrador1_idx` (`Administrador_id_Administrador`),
  CONSTRAINT `fk_Paciente_Administrador1` FOREIGN KEY (`Administrador_id_Administrador`) REFERENCES `administrador` (`id_Administrador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente`
--

LOCK TABLES `paciente` WRITE;
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
/*!40000 ALTER TABLE `paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservaturno`
--

DROP TABLE IF EXISTS `reservaturno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservaturno` (
  `id_reservaTurno` int NOT NULL AUTO_INCREMENT,
  `paciente` varchar(45) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `Paciente_idPaciente` int NOT NULL,
  `turnoEspecialista_id_turnoEspecialista` int NOT NULL,
  PRIMARY KEY (`id_reservaTurno`),
  KEY `fk_reservaTurno_Paciente1_idx` (`Paciente_idPaciente`),
  KEY `fk_reservaTurno_turnoEspecialista1_idx` (`turnoEspecialista_id_turnoEspecialista`),
  CONSTRAINT `fk_reservaTurno_Paciente1` FOREIGN KEY (`Paciente_idPaciente`) REFERENCES `paciente` (`idPaciente`),
  CONSTRAINT `fk_reservaTurno_turnoEspecialista1` FOREIGN KEY (`turnoEspecialista_id_turnoEspecialista`) REFERENCES `turnoespecialista` (`id_turnoEspecialista`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservaturno`
--

LOCK TABLES `reservaturno` WRITE;
/*!40000 ALTER TABLE `reservaturno` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservaturno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `turnoespecialista`
--

DROP TABLE IF EXISTS `turnoespecialista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turnoespecialista` (
  `id_turnoEspecialista` int NOT NULL AUTO_INCREMENT,
  `Fecha` date NOT NULL,
  `Hora` time NOT NULL,
  `horaHasta` time NOT NULL,
  `Especialista_idEspecialista` int NOT NULL,
  PRIMARY KEY (`id_turnoEspecialista`),
  KEY `fk_turnoEspecialista_Especialista1_idx` (`Especialista_idEspecialista`),
  CONSTRAINT `fk_turnoEspecialista_Especialista1` FOREIGN KEY (`Especialista_idEspecialista`) REFERENCES `especialista` (`idEspecialista`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `turnoespecialista`
--

LOCK TABLES `turnoespecialista` WRITE;
/*!40000 ALTER TABLE `turnoespecialista` DISABLE KEYS */;
/*!40000 ALTER TABLE `turnoespecialista` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-12 13:45:11
