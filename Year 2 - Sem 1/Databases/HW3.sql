
CREATE TABLE DEPARTMENT
	(DepartmentId INT PRIMARY KEY,
	DepartmentName VARCHAR(50),

	)



CREATE TABLE EMPLOYEE
	(EmployeeId INT PRIMARY KEY,
	FirstName VARCHAR(50),
	LastName VARCHAR(50),
	Job VARCHAR(50),
	Salary INT
	
	)

CREATE TABLE BRANCH
	(
		BranchId INT PRIMARY KEY,
		City VARCHAR(50),
	    Street VARCHAR(50),
	    Number INT

	)

ALTER TABLE EMPLOYEE
ADD DepartmentId INT
CONSTRAINT FK_EMPLOYEE_DepartmentId
	FOREIGN KEY (DepartmentId)
	REFERENCES DEPARTMENT(DepartmentId)

ALTER TABLE DEPARTMENT
ADD BranchId INT
CONSTRAINT FK_DEPARTMENT_BranchId
	FOREIGN KEY (BranchId)
	REFERENCES BRANCH(BranchId)



CREATE TABLE CLIENT
	(CNP VARCHAR(50) PRIMARY KEY,
	FirstName VARCHAR(50),
	LastName VARCHAR(50),
	PhoneNumber VARCHAR(50)
	)



CREATE TABLE OFFER
	(OfferId INT PRIMARY KEY,
	SDate VARCHAR(50),
	EDate VARCHAR(50)
	)

CREATE TABLE BILL
	(BillId INT PRIMARY KEY,
	 DateofBill VARCHAR(50),
	 ValueofBill INT
	)

ALTER TABLE BILL
ADD EmployeeID INT
CONSTRAINT FK_EMPLOYEE_BILL
	FOREIGN KEY (EmployeeId)
	REFERENCES EMPLOYEE(EmployeeId)

ALTER TABLE BILL
ADD OfferID INT
CONSTRAINT FK_OFFER_BILL
	FOREIGN KEY (OfferId)
	REFERENCES OFFER(OfferId)


CREATE TABLE DESTINATION
	(destId INT PRIMARY KEY,
	 destination_name VARCHAR(50)
	)

CREATE TABLE BILL_CLIENT
	(BillId INT REFERENCES BILL(BillId),
	 CNP VARCHAR(50) REFERENCES CLIENT(CNP),
	 PRIMARY KEY(BillID,CNP)

)
CREATE TABLE OFFER_DESTINATION
	(OfferId INT REFERENCES OFFER(OfferId),
	 destId INT REFERENCES DESTINATION(destId),
	 PRIMARY KEY(OfferId,destId)

)

CREATE TABLE SERVICES_PROVIDER
(
	pId INT PRIMARY KEY,
	 provider_name VARCHAR(50)
)

ALTER TABLE SERVICES_PROVIDER
ADD EmployeeId INT
CONSTRAINT FK_SERVICES_PROVIDER_EmployeeId
	FOREIGN KEY (EmployeeId)
	REFERENCES EMPLOYEE(EmployeeId)

CREATE TABLE ACCOMODATION
(
	 AId INT PRIMARY KEY,
	 acc_name VARCHAR(50),
	 acc_type VARCHAR(50)
)

ALTER TABLE ACCOMODATION
ADD pId INT
CONSTRAINT FK_ACCOMODATION_pId
	FOREIGN KEY (pId)
	REFERENCES  SERVICES_PROVIDER(pId)

ALTER TABLE ACCOMODATION
ADD 
CONSTRAINT FK_ACCOMODATION_destId
	FOREIGN KEY (destId)
	REFERENCES DESTINATION(destId)

CREATE TABLE TRANSPORT
(
	 tId INT PRIMARY KEY,
	 tr_name VARCHAR(50),
	 tr_type VARCHAR(50)
)


ALTER TABLE TRANSPORT
add pId int CONSTRAINT FK_TRANSPORT_pId
	FOREIGN KEY (pId)
	REFERENCES  SERVICES_PROVIDER(pId)

CREATE TABLE TRANSPORT_DESTINATION
	(tId INT REFERENCES TRANSPORT(tID),
	 destId INT REFERENCES DESTINATION(destId),
	 PRIMARY KEY(tId,destId)

)

CREATE TABLE Restaurant
(
	 rId INT NOT NULL,
	 restaurant_name VARCHAR(50),
	 restaurant_addres VARCHAR(50),
	 CONSTRAINT PK_Res PRIMARY KEY (rId) 
)


ALTER TABLE RESTAURANT
	ADD pId INT
	CONSTRAINT FK_Restaurant_pId
	FOREIGN KEY (pId)
	REFERENCES  SERVICES_PROVIDER(pId)




/* inserts */


select * from CLIENT
insert into CLIENT(CNP, FirstName, LastName, PhoneNumber) values ('6020208303911','Chereji', 'Iulia','0721389973')
insert into CLIENT(CNP, FirstName, LastName, PhoneNumber) values ('5020208303911','Olariu', 'Mihai','0721387993')
insert into CLIENT(CNP, FirstName, LastName, PhoneNumber) values ('6010822302921','Stan', 'Ioana','0725387973')
insert into CLIENT(CNP, FirstName, LastName, PhoneNumber) values ('6010923402821','Stan', 'Iulia','0729337973')
insert into CLIENT(CNP, FirstName, LastName, PhoneNumber) values ('6010923402822',NULL,'Iulia','0729337973')

UPDATE CLIENT
SET FirstName='Pop' 
WHERE LastName LIKE 'I__i_'

DELETE 
FROM CLIENT
WHERE FirstName IS NULL

DELETE 
FROM CLIENT
WHERE CNP='6010923402822'


insert into BILL(BillId, DateofBill, ValueofBill) values (1,'08-02-2021',1000)
insert into BILL(BillId, DateofBill, ValueofBill) values (2,'08-12-2020',100)
insert into BILL(BillId, DateofBill, ValueofBill) values (3,'18-12-2020',2000)
insert into BILL(BillId, DateofBill, ValueofBill,EmployeeID,OfferID) values (4,'23-02-2021',4000,1,2)
insert into BILL(BillId, DateofBill, ValueofBill,EmployeeID,OfferID) values (5,'18-10-2010',1000,2,2)
insert into BILL(BillId, DateofBill, ValueofBill,EmployeeID,OfferID) values (6,'08-02-2021',3000,2,2)
insert into BILL(BillId, DateofBill, ValueofBill,EmployeeID,OfferID) values (7,'08-02-2021',3000,2,8)--violate referencial integrity constrain
insert into BILL(BillId, DateofBill, ValueofBill,EmployeeID,OfferID) values (7,'08-02-2011',2070,2,4)
insert into BILL(BillId, DateofBill, ValueofBill,EmployeeID,OfferID) values (8,'28-12-2011',4070,3,4)
select * from BILL


insert into BILL_CLIENT(BillId, CNP) values (1,'6020208303911' )
insert into BILL_CLIENT(BillId, CNP) values (3, '6020208303911')
insert into BILL_CLIENT(BillId, CNP) values (2, '5020208303911')
insert into BILL_CLIENT(BillId, CNP) values (3, '5020208303911')
insert into BILL_CLIENT(BillId,CNP) values(4,'6010822302921')
insert into BILL_CLIENT(BillId,CNP) values(5,'6010822302921')
select * from BILL_CLIENT



insert into EMPLOYEE(EmployeeId,FirstName,LastName,Job,Salary) values (2,'Ion','Pop','boss',123)
insert into EMPLOYEE(EmployeeId,FirstName,LastName,Job,Salary) values (3,'Ioan','Popa','adjunct',120)
insert into EMPLOYEE(EmployeeId,FirstName,LastName,Job,Salary) values (4,'Ioana','Popas','salesperson',50)
insert into EMPLOYEE(EmployeeId,FirstName,LastName,Job,Salary) values (1,'Ioana','Popasa','salesperson',50)
insert into EMPLOYEE(EmployeeId,FirstName,LastName,Job,Salary) values (5,'Iulia','Pras','provider',100)
insert into EMPLOYEE(EmployeeId,FirstName,LastName,Job,Salary) values (6,'Ioana','Stam','provider',100)
insert into EMPLOYEE(EmployeeId,FirstName,LastName,Job,Salary) values (7,'Iulia','Tarta','provider',150)
insert into EMPLOYEE(EmployeeId,FirstName,LastName,Job,Salary,DepartmentId) values (8,'Iulian','Tar','salesperson',50,2)
insert into EMPLOYEE(EmployeeId,FirstName,LastName,Job,Salary,DepartmentId) values (9,'Iuliana','Bob','salesperson',50,2)
select * from EMPLOYEE

delete 
from EMPLOYEE
where EmployeeId BETWEEN 3 AND 4


insert into DEPARTMENT(DepartmentId, DepartmentName) values (1, 'human rescources')
insert into DEPARTMENT(DepartmentId, DepartmentName) values (2, 'sales')
insert into DEPARTMENT(DepartmentId, DepartmentName) values (3, 'CEO')
insert into DEPARTMENT(DepartmentId, DepartmentName) values (4, 'provision')
select * from DEPARTMENT

update DEPARTMENT
set BranchId=2
where DepartmentId=1




insert into DESTINATION(destId, destination_name) values (1, 'Paris')
insert into DESTINATION(destId, destination_name) values (2, 'Rome')
insert into DESTINATION(destId, destination_name) values (3, 'Bucharest')
insert into DESTINATION(destId,destination_name) values (4, 'LA')
select * from DESTINATION


insert into OFFER(OfferId,SDate,EDate) values (1, '18.02.2020', '23.02.2020')
insert into OFFER(OfferId,SDate,EDate) values (2, '15.05.2021', '20.05.2021')
insert into OFFER(OfferId,SDate,EDate) values (3, '09.03.2021', '11.03.2021')
insert into OFFER(OfferId,SDate,EDate) values (4, '09.04.2022', '11.04.2022')
select * from OFFER

insert into OFFER_DESTINATION(OfferId,destId) values(1,1)
insert into OFFER_DESTINATION(OfferId,destId) values(2,2)
insert into OFFER_DESTINATION(OfferId,destId) values(1,3)
insert into OFFER_DESTINATION(OfferId,destId) values(4,1)
select * from OFFER_DESTINATION

update EMPLOYEE
set Job='CEO'
where FirstName ='Ion' AND LastName='Pop'

update OFFER
set SDate = '15.04.2022'
where OfferId >= 2

update TRANSPORT
set pId=2
where tId=1 or tId=2



insert into TRANSPORT(tId,tr_name,tr_type) values (1, 'WizzAircraft 1', 'airplane')
insert into TRANSPORT(tId,tr_name,tr_type) values (2, 'WizzAircraft 2', 'airplane')
insert into TRANSPORT(tId,tr_name,tr_type) values (3, 'Fany Bus 1', 'bus')
insert into TRANSPORT(tId,tr_name,tr_type) values (4, 'Titanic', 'ship')
select * from TRANSPORT

update TRANSPORT
set tr_type='Airplane'
where tId in (1,2)

insert into TRANSPORT_DESTINATION(tId,destId) values (1,1)
insert into TRANSPORT_DESTINATION(tId,destId) values (2,2)
insert into TRANSPORT_DESTINATION(tId,destId) values (3,1)
insert into TRANSPORT_DESTINATION(tId,destId) values (4,4)
insert into TRANSPORT_DESTINATION(tId,destId) values (3,2)
select * from TRANSPORT_DESTINATION

insert into SERVICES_PROVIDER(pId,provider_name) values (1,'Plaza Athenee Company')
insert into SERVICES_PROVIDER(pId,provider_name) values (2,'WizzAir')
insert into SERVICES_PROVIDER(pId,provider_name) values (3,'Rome Apartments')
insert into SERVICES_PROVIDER(pId,provider_name) values (4,'Fany Transport')
insert into SERVICES_PROVIDER(pId,provider_name) values (5,'Deluxe Ships')
insert into SERVICES_PROVIDER(pId,provider_name) values (6,'Paris Accomodation')
insert into SERVICES_PROVIDER(pId,provider_name) values (7,'Bucharest Accomodation')
insert into SERVICES_PROVIDER(pId,provider_name) values (8,'LA Accomodation')
select * from SERVICES_PROVIDER

update SERVICES_PROVIDER
set EmployeeId=6
where pId>=5


insert into ACCOMODATION(AId,acc_name,acc_type,pId, destId) values (1, 'Plaza Athenee','hotel',1,1)
insert into ACCOMODATION(AId,acc_name,acc_type,pId, destId) values (3, 'Paris Hotel','hotel',6,1)
insert into ACCOMODATION(AId,acc_name,acc_type,pId, destId) values (2, 'Rome 1 ','apartment',3,2)
insert into ACCOMODATION(AId,acc_name,acc_type,pId, destId) values (4, 'City Hotel ','hotel',7,3)
insert into ACCOMODATION(AId,acc_name,acc_type,pId, destId) values (5, 'LA Best Apartments ','apartment',8,4)
insert into ACCOMODATION(AId,acc_name,acc_type,pId, destId) values (6, 'Plaza Athenee 2','hotel',1,1)
select * from ACCOMODATION



insert into BRANCH(BranchId,City,Street,Number) values (1,'New York','Principal Street',11)
insert into BRANCH(BranchId,City,Street,Number) values (2,'Cluj','Cuza Voda',18)
insert into BRANCH(BranchId,City,Street,Number) values (3,'Bucharest','Unirii',1)
select * from BRANCH

/*PROCEDURES */

--a.modify type of a column
Go
CREATE or ALTER PROC uspModifyCol
AS 
BEGIN
	ALTER TABLE BRANCH
	ALTER COLUMN Number tinyint
END
exec uspModifyCol

-- reverse a
Go
CREATE or ALTER PROC uspRevertModifyCol
AS 
BEGIN
	ALTER TABLE BRANCH
	ALTER COLUMN Number INT
END
exec uspRevertModifyCol


-- b. add/remove column
go
CREATE or ALTER PROC uspAddColumn
AS
BEGIN
	ALTER TABLE ACCOMODATION
	ADD Rating INT
END
exec uspAddColumn


-- reverse b
go
CREATE OR ALTER PROC uspDeleteColumn
As
BEGIN
	ALTER TABLE ACCOMODATION
	DROP COLUMN Rating
END
exec uspDeleteColumn

--c.add / remove a DEFAULT constraint
go
CREATE OR ALTER PROC uspAddDefaultConstraint
As
BEGIN
	ALTER TABLE EMPLOYEE
	ADD CONSTRAINT def_sal DEFAULT 1000 for Salary
END

exec uspAddDefaultConstraint

-- reverse c
go
CREATE OR ALTER PROC uspDeleteDefaultConstraint
As
BEGIN
	ALTER TABLE EMPLOYEE
	DROP CONSTRAINT def_sal 
END
exec uspDeleteDefaultConstraint

--d. add / remove a primary key;
go
CREATE OR ALTER PROC uspDeletePk
AS
BEGIN
	ALTER TABLE Restaurant
	Drop CONSTRAINT PK_Res 
	
END
exec uspDeletePk

-- reverse d
go
CREATE OR ALTER PROC uspAddPk
AS
BEGIN
	ALTER TABLE Restaurant
	ADD CONSTRAINT PK_Res PRIMARY KEY (rId) 
END
exec uspAddPk

--e. add / remove a candidate key;
go
CREATE OR ALTER PROC uspAddCandidateKey
As
BEGIN
	ALTER TABLE department
	ADD CONSTRAINT Unique_dep_ID_NAME UNIQUE (DepartmentId, DepartmentName)
END
exec uspAddCandidateKey

--reverse e
go
CREATE OR ALTER PROC uspDeleteCandidateKey
As
BEGIN
	ALTER TABLE DEPARTMENT
	DROP CONSTRAINT Unique_dep_ID_NAME 
END
exec uspDeleteCandidateKey

--f. add / remove a foreign key;

go
CREATE OR ALTER PROC uspDeleteFk
AS
BEGIN 
	ALTER TABLE ACCOMODATION
	DROP CONSTRAINT FK_ACCOMODATION_destId
END
exec uspDeleteFk
--reverse f

go 
CREATE OR ALTER PROC uspAddFk
AS
BEGIN
	ALTER TABLE ACCOMODATION
	ADD CONSTRAINT FK_ACCOMODATION_destId
	FOREIGN KEY (destId)
	REFERENCES DESTINATION(destId)
end
exec uspAddFk


--g. create / drop a table.
go
CREATE OR ALTER PROC uspAddTable
As
BEGIN
  	CREATE TABLE SpecialtyMeal
(
	 mId int primary key,
	 meal_name Varchar(50),
	 
)
END
		
exec uspAddTable


--reverse g
go
CREATE OR ALTER PROC uspDropTable
As
BEGIN
	drop table SpecialtyMeal
END	
exec uspDropTable

--main procedure

go
CREATE TABLE VERSION_TABLE
(
	crtVersion INT default 0,
	proc_name VARCHAR(50),
	reverse_proc_name VARCHAR(50),
	targetVersion INT 

	
)
INSERT INTO VERSION_TABLE(targetVersion,proc_name,reverse_proc_name, crtVersion) VALUES (0,'','', 1)
INSERT INTO VERSION_TABLE(targetVersion, proc_name, reverse_proc_name) VALUES (1, 'uspModifyCol', 'uspRevertModifyCol');
INSERT INTO VERSION_TABLE(targetVersion, proc_name, reverse_proc_name) VALUES (2, 'uspAddColumn', 'uspDeleteColumn');
INSERT INTO VERSION_TABLE(targetVersion, proc_name, reverse_proc_name) VALUES (3, 'uspAddDefaultConstraint', 'uspDeleteDefaultConstraint');
INSERT INTO VERSION_TABLE(targetVersion, proc_name, reverse_proc_name) VALUES (4, 'uspDeletePk', 'uspAddPk');
INSERT INTO VERSION_TABLE(targetVersion, proc_name, reverse_proc_name) VALUES (5, 'uspAddCandidateKey', 'uspDeleteCandidateKey');
INSERT INTO VERSION_TABLE(targetVersion, proc_name, reverse_proc_name) VALUES (6, 'uspDeleteFk', 'uspAddFk');
INSERT INTO VERSION_TABLE(targetVersion, proc_name, reverse_proc_name) VALUES (7, 'uspAddTable', 'uspDropTable');




go
CREATE OR ALTER PROC mainProcedure(@newVersion INT)
AS	
begin
	DECLARE @current_version INT
	Select @current_version=VT.targetVersion
	from VERSION_TABLE VT
	where VT.crtVersion=1

	DECLARE @procedure_name VARCHAR(50)
	DECLARE @reverse_procedure_name VARCHAR(50)

	IF @newVersion<0 OR @newVersion>7 
		BEGIN 
			PRINT 'Invalid version'
			RETURN
		END
	ELSE 
		BEGIN
			UPDATE VERSION_TABLE
			SET crtVersion=0 
			WHERE targetVersion=@current_version

			IF @newVersion > @current_version
			BEGIN	
				WHILE @newVersion>@current_version
				BEGIN 
					
					SET @current_version = @current_version + 1

					SELECT @procedure_name = proc_name
					FROM VERSION_TABLE
					WHERE targetVersion=@current_version

					EXEC @procedure_name
				END
			END
			ELSE
			BEGIN
				WHILE @newVersion<@current_version
				BEGIN 
					
					SELECT @reverse_procedure_name = reverse_proc_name
					FROM VERSION_TABLE
					WHERE targetVersion=@current_version

					SET @current_version = @current_version - 1

					EXEC @reverse_procedure_name
					 
				END
			END

			

			UPDATE VERSION_TABLE 
			SET crtVersion=1
			WHERE targetVersion=@newVersion

			RETURN
		end
		
end


go

exec mainProcedure 2

select * from VERSION_TABLE
select * from SpecialtyMeal
