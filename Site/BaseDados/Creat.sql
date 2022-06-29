-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema carvago
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema carvago
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `carvago` DEFAULT CHARACTER SET utf8 ;
USE `carvago` ;

-- -----------------------------------------------------
-- Table `carvago`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carvago`.`User` (
  `idUser` INT NOT NULL,
  `Nome` VARCHAR(45) NULL,
  `Email` VARCHAR(255) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUser`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `carvago`.`Filtros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carvago`.`Filtros` (
  `idFiltros` INT NOT NULL,
  `User_idUser` INT NOT NULL,
  `AnoMinimo` INT NOT NULL,
  `AnoMaximo` INT NOT NULL,
  `PrecoMinimo` DOUBLE NOT NULL,
  `PrecoMaximo` DOUBLE NOT NULL,
  `Combustivel` VARCHAR(45) NOT NULL,
  `KM_Minimo` INT NOT NULL,
  `KM_Maximo` INT NOT NULL,
  `Filtroscol` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idFiltros`, `User_idUser`),
  INDEX `fk_Filtros_User1_idx` (`User_idUser` ASC) VISIBLE,
  CONSTRAINT `fk_Filtros_User1`
    FOREIGN KEY (`User_idUser`)
    REFERENCES `carvago`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `carvago`.`Carros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carvago`.`Carros` (
  `idCarros` INT NOT NULL,
  `Anunciante` VARCHAR(45) NULL,
  `Marca` VARCHAR(45) NOT NULL,
  `Modelo` VARCHAR(45) NOT NULL,
  `Versao` VARCHAR(45) NULL,
  `Combustivel` VARCHAR(45) NULL,
  `Mes_Registo` VARCHAR(45) NULL,
  `Ano` INT NULL,
  `Quilometros` INT NULL,
  `Cilindrada` INT NULL,
  `Potencia` INT NULL,
  `Cor` VARCHAR(45) NULL,
  `Tipo_Cor` VARCHAR(45) NULL,
  `Tipo_Caixa` VARCHAR(45) NULL,
  `Num_Portas` INT NULL,
  `Origem` VARCHAR(45) NULL,
  `Condicao` VARCHAR(45) NULL,
  `Preco` DOUBLE NOT NULL,
  PRIMARY KEY (`idCarros`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `carvago`.`UserCarros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `carvago`.`UserCarros` (
  `User_idUser` INT NOT NULL,
  `Carros_idCarros` INT NOT NULL,
  PRIMARY KEY (`User_idUser`, `Carros_idCarros`),
  INDEX `fk_UserCarros_Carros1_idx` (`Carros_idCarros` ASC) VISIBLE,
  CONSTRAINT `fk_UserCarros_User`
    FOREIGN KEY (`User_idUser`)
    REFERENCES `carvago`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_UserCarros_Carros1`
    FOREIGN KEY (`Carros_idCarros`)
    REFERENCES `carvago`.`Carros` (`idCarros`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
