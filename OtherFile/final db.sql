-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  ven. 06 sep. 2019 à 16:15
-- Version du serveur :  5.7.17
-- Version de PHP :  5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `gestibank`
--
CREATE DATABASE IF NOT EXISTS `gestibank` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `gestibank`;

-- --------------------------------------------------------

--
-- Structure de la table `admin`
--

CREATE TABLE `admin` (
  `ID` varchar(10) NOT NULL,
  `NOM` varchar(30) DEFAULT NULL,
  `PRENOM` varchar(20) DEFAULT NULL,
  `TYPE_USER` enum('ADMIN','AGENT','CLIENT') DEFAULT NULL,
  `mail` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `admin`
--

INSERT INTO `admin` (`ID`, `NOM`, `PRENOM`, `TYPE_USER`, `mail`) VALUES
('12', 'admin', 'admina', 'ADMIN', 'adim');

-- --------------------------------------------------------

--
-- Structure de la table `agent`
--

CREATE TABLE `agent` (
  `ID` varchar(10) NOT NULL,
  `NOM` varchar(30) DEFAULT NULL,
  `PRENOM` varchar(20) DEFAULT NULL,
  `TYPE_USER` enum('ADMIN','AGENT','CLIENT') DEFAULT NULL,
  `MAIL` varchar(50) DEFAULT NULL,
  `TEL` varchar(15) DEFAULT NULL,
  `DEBUT_CONTRAT` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE `client` (
  `ID` varchar(10) NOT NULL,
  `NOM` varchar(30) DEFAULT NULL,
  `PRENOM` varchar(20) DEFAULT NULL,
  `TYPE_USER` enum('ADMIN','AGENT','CLIENT') DEFAULT NULL,
  `MAIL` varchar(50) DEFAULT NULL,
  `TEL` varchar(15) DEFAULT NULL,
  `ADRESSE` varchar(100) DEFAULT NULL,
  `JUSTIFICATIF` varchar(30) DEFAULT NULL,
  `id_agent` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `compte`
--

CREATE TABLE `compte` (
  `id_compte` varchar(20) NOT NULL,
  `id_client` varchar(10) NOT NULL,
  `type_compte` enum('COURANT','DECOUVERT','INTERET') NOT NULL,
  `rib` varchar(24) NOT NULL,
  `solde` float NOT NULL,
  `date_creation` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `demande_creacompte`
--

CREATE TABLE `demande_creacompte` (
  `ID` varchar(10) NOT NULL,
  `NOM` varchar(30) NOT NULL,
  `PRENOM` varchar(20) NOT NULL,
  `MAIL` varchar(50) NOT NULL,
  `TEL` varchar(15) NOT NULL,
  `ADRESSE` varchar(100) NOT NULL,
  `JUSTIFICATIF` varchar(30) NOT NULL,
  `affect` varchar(15) DEFAULT NULL,
  `valide` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `login`
--

CREATE TABLE `login` (
  `ID` varchar(10) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `TYPE_USER` enum('ADMIN','AGENT','CLIENT') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `login`
--

INSERT INTO `login` (`ID`, `Password`, `TYPE_USER`) VALUES
('007', '*BD885142404C127AC29793EE3FBB1FDB01D2B25F', 'AGENT'),
('12', '*BD885142404C127AC29793EE3FBB1FDB01D2B25F', 'ADMIN');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `agent`
--
ALTER TABLE `agent`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `compte`
--
ALTER TABLE `compte`
  ADD PRIMARY KEY (`id_compte`);

--
-- Index pour la table `demande_creacompte`
--
ALTER TABLE `demande_creacompte`
  ADD PRIMARY KEY (`ID`);

--
-- Index pour la table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`ID`,`TYPE_USER`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
