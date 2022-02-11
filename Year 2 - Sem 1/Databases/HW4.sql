
--implement a set of stored procedures for running tests and storing their results
if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunTables_Tables]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunTables] DROP CONSTRAINT FK_TestRunTables_Tables

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestTables_Tables]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestTables] DROP CONSTRAINT FK_TestTables_Tables

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunTables_TestRuns]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunTables] DROP CONSTRAINT FK_TestRunTables_TestRuns

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunViews_TestRuns]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunViews] DROP CONSTRAINT FK_TestRunViews_TestRuns

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestTables_Tests]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestTables] DROP CONSTRAINT FK_TestTables_Tests

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestViews_Tests]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestViews] DROP CONSTRAINT FK_TestViews_Tests

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunViews_Views]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunViews] DROP CONSTRAINT FK_TestRunViews_Views

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestViews_Views]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestViews] DROP CONSTRAINT FK_TestViews_Views

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[Tables]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [Tables]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestRunTables]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestRunTables]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestRunViews]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestRunViews]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestRuns]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestRuns]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestTables]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestTables]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestViews]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestViews]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[Tests]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [Tests]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[Views]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [Views]

GO



CREATE TABLE [Tables] (

	[TableID] [int] IDENTITY (1, 1) NOT NULL ,

	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestRunTables] (

	[TestRunID] [int] NOT NULL ,

	[TableID] [int] NOT NULL ,

	[StartAt] [datetime] NOT NULL ,

	[EndAt] [datetime] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestRunViews] (

	[TestRunID] [int] NOT NULL ,

	[ViewID] [int] NOT NULL ,

	[StartAt] [datetime] NOT NULL ,

	[EndAt] [datetime] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestRuns] (

	[TestRunID] [int] IDENTITY (1, 1) NOT NULL ,

	[Description] [nvarchar] (2000) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,

	[StartAt] [datetime] NULL ,

	[EndAt] [datetime] NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestTables] (

	[TestID] [int] NOT NULL ,

	[TableID] [int] NOT NULL ,

	[NoOfRows] [int] NOT NULL ,

	[Position] [int] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestViews] (

	[TestID] [int] NOT NULL ,

	[ViewID] [int] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [Tests] (

	[TestID] [int] IDENTITY (1, 1) NOT NULL ,

	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [Views] (

	[ViewID] [int] IDENTITY (1, 1) NOT NULL ,

	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 

) ON [PRIMARY]

GO



ALTER TABLE [Tables] WITH NOCHECK ADD 

	CONSTRAINT [PK_Tables] PRIMARY KEY  CLUSTERED 

	(

		[TableID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRunTables] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestRunTables] PRIMARY KEY  CLUSTERED 

	(

		[TestRunID],

		[TableID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRunViews] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestRunViews] PRIMARY KEY  CLUSTERED 

	(

		[TestRunID],

		[ViewID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRuns] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestRuns] PRIMARY KEY  CLUSTERED 

	(

		[TestRunID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestTables] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestTables] PRIMARY KEY  CLUSTERED 

	(

		[TestID],

		[TableID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestViews] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestViews] PRIMARY KEY  CLUSTERED 

	(

		[TestID],

		[ViewID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [Tests] WITH NOCHECK ADD 

	CONSTRAINT [PK_Tests] PRIMARY KEY  CLUSTERED 

	(

		[TestID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [Views] WITH NOCHECK ADD 

	CONSTRAINT [PK_Views] PRIMARY KEY  CLUSTERED 

	(

		[ViewID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRunTables] ADD 

	CONSTRAINT [FK_TestRunTables_Tables] FOREIGN KEY 

	(

		[TableID]

	) REFERENCES [Tables] (

		[TableID]

	) ON DELETE CASCADE  ON UPDATE CASCADE ,

	CONSTRAINT [FK_TestRunTables_TestRuns] FOREIGN KEY 

	(

		[TestRunID]

	) REFERENCES [TestRuns] (

		[TestRunID]

	) ON DELETE CASCADE  ON UPDATE CASCADE 

GO



ALTER TABLE [TestRunViews] ADD 

	CONSTRAINT [FK_TestRunViews_TestRuns] FOREIGN KEY 

	(

		[TestRunID]

	) REFERENCES [TestRuns] (

		[TestRunID]

	) ON DELETE CASCADE  ON UPDATE CASCADE ,

	CONSTRAINT [FK_TestRunViews_Views] FOREIGN KEY 

	(

		[ViewID]

	) REFERENCES [Views] (

		[ViewID]

	) ON DELETE CASCADE  ON UPDATE CASCADE 

GO



ALTER TABLE [TestTables] ADD 

	CONSTRAINT [FK_TestTables_Tables] FOREIGN KEY 

	(

		[TableID]

	) REFERENCES [Tables] (

		[TableID]

	) ON DELETE CASCADE  ON UPDATE CASCADE ,

	CONSTRAINT [FK_TestTables_Tests] FOREIGN KEY 

	(

		[TestID]

	) REFERENCES [Tests] (

		[TestID]

	) ON DELETE CASCADE  ON UPDATE CASCADE 

GO



ALTER TABLE [TestViews] ADD 

	CONSTRAINT [FK_TestViews_Tests] FOREIGN KEY 

	(

		[TestID]

	) REFERENCES [Tests] (

		[TestID]

	),

	CONSTRAINT [FK_TestViews_Views] FOREIGN KEY 

	(

		[ViewID]

	) REFERENCES [Views] (

		[ViewID]

	)

GO

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
ADD destId Int
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
	 CONSTRAINT PK_Res PRIMARY KEY (rId,restaurant_addres) 
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
insert into DESTINATION(destId, destination_name) values (5, 'Satu Mare')
insert into DESTINATION(destId, destination_name) values (6, 'New York')
insert into DESTINATION(destId, destination_name) values (7, 'Budapest')
insert into DESTINATION(destId,destination_name) values (8, 'Cluj')
insert into DESTINATION(destId, destination_name) values (9, 'Barcelona')
insert into DESTINATION(destId,destination_name) values (0, 'Athens')



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
delete from TRANSPORT_DESTINATION

insert into SERVICES_PROVIDER(pId,provider_name) values (1,'Plaza Athenee Company')
insert into SERVICES_PROVIDER(pId,provider_name) values (2,'WizzAir')
insert into SERVICES_PROVIDER(pId,provider_name) values (3,'Rome Apartments')
insert into SERVICES_PROVIDER(pId,provider_name) values (4,'Fany Transport')
insert into SERVICES_PROVIDER(pId,provider_name) values (5,'Deluxe Ships')
insert into SERVICES_PROVIDER(pId,provider_name) values (6,'Paris Accomodation')
insert into SERVICES_PROVIDER(pId,provider_name) values (7,'Bucharest Accomodation')
insert into SERVICES_PROVIDER(pId,provider_name) values (8,'LA Accomodation')
insert into SERVICES_PROVIDER(pId,provider_name) values (9,'Satu Mare Accomodation')
insert into SERVICES_PROVIDER(pId,provider_name) values (0,'USA Ships')
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

-----------hw4------------

--a view with a SELECT statement that has a GROUP BY clause and operates on at least 2 tables.
go
create or alter view vRestpid
as
	select S.pId, count(*) as restaurant_by_sp
	from Restaurant R, SERVICES_PROVIDER S, DESTINATION d
	where R.pId=S.pId and d.destId%2=1
	group by S.pId


--a view with a SELECT statement operating on at least 2 tables;
go
create or alter view vAccDest
as
	select A.acc_name, D.destination_name
	from ACCOMODATION A INNER JOIN DESTINATION D ON A.destId=D.destId and A.pId=1
	

--a view with a SELECT statement operating on one table;
go
create or alter view vAccInDest1
as
	select *
	from ACCOMODATION A
	WHERE A.destId % 2 =1
	



go

CREATE OR ALTER PROCEDURE uspGenericInsert @tableName VARCHAR(50), @nrRows INT AS
BEGIN

	DECLARE @i INT
	SET @i = 1


	declare @dest_name varchar(50)

	declare @AId int
	declare @acc_name varchar(50)
	declare @acc_type varchar(50)
	declare @destId int
	declare @pId int

	declare @rId int
	declare @rest_name varchar(50)
	declare @rest_addr varchar(50)

	WHILE @i <= @nrRows
		BEGIN
			if @tableName='Destination'
			begin
					set @destId=@i
					set @dest_name='destination'+ convert(varchar(50), @destId)
					insert into DESTINATION(destId,destination_name) values (@destId,@dest_name)
			end

			if @tableName='Accomodation'
			begin
					set @AId=@i
					set @acc_name='acc name'+convert(varchar(50), @i)
					set @acc_type='acc type'+convert(varchar(50), @i)
					set @destId=@i%10+1
					set @pId=@i%10
					insert into ACCOMODATION(AId,acc_name,acc_type,destId,pId) values (@AId,@acc_name,@acc_type,@destId, @pId)
			end

			if @tableName='Restaurant'
			begin
					set @rId=@i
					set @rest_name='restaurant '+convert(varchar(50), @i)
					set @rest_addr='address '+convert(varchar(50), @i)
					set @pId=@i%10
					insert into Restaurant(rId,restaurant_name,restaurant_addres,pId) values(@rId, @rest_name, @rest_addr,@pid)

			end

			SET @i = @i + 1

		END
END
----------

create table ForeignKeys
(
	tableName varchar(100),
	foreign_key varchar(100)

)

create table PrimaryKeys
(
	tableName varchar(100),
	primary_key varchar(100)
)
delete from ForeignKeys


go
create or alter procedure insertFKTable as
begin
	declare @tableName varchar(100), @fk varchar(100)

	declare FKCursor cursor for
	select distinct TABLE_NAME,COLUMN_NAME 
	FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS rc INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE kc 
	ON rc.CONSTRAINT_CATALOG=kc.CONSTRAINT_CATALOG
	and rc.CONSTRAINT_NAME=kc.CONSTRAINT_NAME  

	OPEN FKCursor
	fetch FKCursor into @tableName, @fk
	while @@FETCH_STATUS=0
	begin 
		insert into ForeignKeys(tableName,foreign_key) values(@tableName,@fk)
		fetch FKCursor into @tableName, @fk
	end
	close FKCursor
	deallocate FKCursor
end


go
create or alter procedure insertPKTable as
begin
	declare @tableName varchar(100), @pk varchar(100)
	declare PKCursor cursor for
	select distinct C.TABLE_NAME,COLUMN_NAME
	FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS T JOIN INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE C  
	ON C.CONSTRAINT_NAME=T.CONSTRAINT_NAME  
	where t.CONSTRAINT_TYPE='PRIMARY KEY' and t.CONSTRAINT_NAME=c.CONSTRAINT_NAME 

	OPEN PKCursor
	fetch PKCursor into @tableName, @pk
	while @@FETCH_STATUS=0
	begin 
		insert into PrimaryKeys(tableName,primary_key) values(@tableName,@pk)
		fetch PKCursor into @tableName, @pk
	end
	close PKCursor
	deallocate PKCursor
end


go
create or alter procedure try_generic_insert @tableName varchar(100), @nrRows int
as
begin
	DECLARE @i INT
	SET @i = 1
	declare @columnName varchar(50), @columnType varchar(20), @insert_cmd varchar(200);
	DECLARE @Min INT = 1, @Max INT = 1000000;

	while @i <= @nrRows
	begin
		SET @insert_cmd = 'insert into ' + @tableName + ' values ('
	
		DECLARE TableCursor CURSOR FOR	
		SELECT COLUMN_NAME, DATA_TYPE
		FROM INFORMATION_SCHEMA.COLUMNS 
		WHERE TABLE_NAME = @tableName
	
		OPEN TableCursor
		FETCH TableCursor INTO @ColumnName, @columnType	
		WHILE @@FETCH_STATUS=0
		BEGIN
			IF @columnType = 'varchar'
			BEGIN
				DECLARE @RandomString varchar(10);
				DECLARE  @ok1 INT = 1, @checkPK1 nvarchar (200);
				--check for pk
				WHILE @ok1 != 0
					BEGIN
						SET @RandomString = CONVERT(varchar(36), NEWID());
						SET @checkPK1 = 'SELECT @nrok=COUNT(*) FROM ' + @tableName + ' WHERE ' + @ColumnName + ' = ' + ' '''+
							@RandomString+' ''';
						EXECUTE sp_executesql @checkPK1, N'@nrok INT OUTPUT', @nrok=@ok1 OUTPUT;
					END
				SET @insert_cmd = @insert_cmd + '''' +  @RandomString + '''';

			END

			IF @columnType = 'int'
			begin
				DECLARE @isFK nvarchar(20) = '';

				SELECT @isFK = F.tableName 
				from ForeignKeys F 
				WHERE F.foreign_key = @columnName
				
			
				-- if the current column is not a foreign key , we add to the insert cmd a random nr
				IF @isFK = ''
				BEGIN
					SET @insert_cmd = @insert_cmd + CONVERT(varchar(10), FLOOR( RAND() * (@Max - @Min))+@Min);
				END

				ELSE
				-- if the current column is a key
				BEGIN
					DECLARE @refTable nvarchar(100) = '';
		
					--get the referenced table
					SELECT @refTable = P.tableName 
					from PrimaryKeys P 
					where P.tableName != @tableName AND P.primary_key = @columnName
				
				
					-- if the referenced table is empty, it means that it is the primary key
					-- otherwise, we pick a random value from the referenced table and add it
					IF @refTable != '' 
					BEGIN
						DECLARE @randomValue int;
						DECLARE @cmd nvarchar(200);
						DECLARE @col nvarchar(200);

						SET @cmd = 'SELECT TOP 1 @col=' + @columnName + ' FROM ' + @refTable + ' ORDER BY NEWID()'
			
						EXECUTE sp_executesql @cmd, 
						N'@col int OUTPUT', @col=@randomValue OUTPUT;
					
						SET @insert_cmd = @insert_cmd+ CONVERT(varchar(10), @randomValue);
						
					END
					ELSE 
					BEGIN
						-- if this is a primary key, we have to check that it won't be duplicated.
						DECLARE @randomPK int, @ok INT = 1, @checkPK nvarchar (200);
				
						WHILE @ok != 0
						BEGIN
							SET @randomPK = FLOOR( RAND() * (@Max - @Min))+@Min;
							SET @checkPK = 'SELECT @nrok=COUNT(*) FROM ' + @tableName + ' WHERE ' + @ColumnName + ' = ' + 
								CONVERT(varchar(50), @randomPK);
							EXECUTE sp_executesql @checkPK, N'@nrok INT OUTPUT', @nrok=@ok OUTPUT;
						END

						SET @insert_cmd = @insert_cmd + CONVERT(varchar(50), @randomPK);
					
					END

			END
			
			end

			FETCH TableCursor INTO @ColumnName, @columnType
			-- if the last fetch did fetch us new data, it means that there are more columns and we have to add a comma
			-- otherwise we close the paranthesis
			IF @@FETCH_STATUS = 0
			BEGIN
				SET @insert_cmd = @insert_cmd + ', ';
			END
			ELSE 
			BEGIN
				SET @insert_cmd = @insert_cmd + ')';
			END

			
		END
	
		EXEC (@insert_cmd)
		CLOSE TableCursor
		DEALLOCATE TableCursor
		-- increase the contor, go to the next row
		SET @i = @i + 1
		
	END
		
end



go
CREATE OR ALTER PROCEDURE uspSeeView @viewName VARCHAR(50) AS
BEGIN
	declare @cmd NVARCHAR(100)
	set @cmd='SELECT * FROM '+@viewName;
	exec(@cmd)
	
end



go
CREATE OR ALTER PROCEDURE uspDeleteRows @tableName varchar(50)
as
	begin
		declare @cmd NVARCHAR(100)
		set @cmd = N'DELETE FROM ' + @tableName;
		exec sys.sp_executesql @cmd

end



-----------------------------------------------------------------------------------------------------------------

insert into Views(Name) values ('vAccInDest1'),('vRestpid'), ('vAccDest')
insert into Tables(Name) values  ('Destination'),('Accomodation'), ('Restaurant')
insert into Tests values ('test_10'),('test_50'),('test_100'),('test_500')



INSERT INTO TestViews(TestID,ViewID) VALUES (1,1)
INSERT INTO TestViews(TestID,ViewID) VALUES (1,2)
INSERT INTO TestViews(TestID,ViewID) VALUES (1,3)
INSERT INTO TestViews(TestID,ViewID) VALUES (2,1)
INSERT INTO TestViews(TestID,ViewID) VALUES (2,2)
INSERT INTO TestViews(TestID,ViewID) VALUES (2,3)
INSERT INTO TestViews(TestID,ViewID) VALUES (3,1)
INSERT INTO TestViews(TestID,ViewID) VALUES (3,2)
INSERT INTO TestViews(TestID,ViewID) VALUES (3,3)
INSERT INTO TestViews(TestID,ViewID) VALUES (4,1)
INSERT INTO TestViews(TestID,ViewID) VALUES (4,2)
INSERT INTO TestViews(TestID,ViewID) VALUES (4,3)



INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (1,1,10,3)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (1,2,10,2)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (1,3,10,1)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (2,1,50,3)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (2,2,50,2)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (2,3,50,1)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (3,1,100,3)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (3,2,100,2)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (3,3,100,1)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (4,1,500,3)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (4,2,500,2)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (4,3,500,1)



GO

DELETE FROM TestRuns
DELETE FROM TestRunTables
DELETE FROM TestRunViews
DELETE FROM TestTables
DELETE FROM TestViews
DELETE FROM Tests
DELETE FROM Views
DELETE FROM Tables

drop table TestRuns
drop table TestRunTables
drop table TestRunViews
drop table TestTables
drop table TestViews
drop table Tests
drop table Views
drop table Tables
GO


-----main procedure---------
go
CREATE OR ALTER PROCEDURE mainTest @testID INT
AS
BEGIN
	INSERT INTO TestRuns(Description,StartAt,EndAt) VALUES ((SELECT Name FROM Tests WHERE TestID=@testID),GETDATE(),GETDATE())
	DECLARE @testRunID INT
	SET @testRunID=(SELECT MAX(TestRunID) FROM TestRuns)

	DECLARE @nrRows INT
	DECLARE @tableID INT
	DECLARE @tableName VARCHAR(30)
	DECLARE @viewID INT
	DECLARE @viewName VARCHAR(30)
	DECLARE @startAt DATETIME
	DECLARE @endAt DATETIME
	

	--test delete 
	DECLARE testDeleteCursor CURSOR FOR
	SELECT TableID
	FROM TestTables
	WHERE TestID=@testID
	ORDER BY Position ASC

	OPEN testDeleteCursor

	FETCH NEXT 
	FROM testDeleteCursor
	INTO @tableID

	WHILE @@FETCH_STATUS=0
	BEGIN
		SET @tableName=(SELECT Name 
		FROM Tables WHERE 
		TableID=@tableID)

		EXEC uspDeleteRows @tableName

		FETCH NEXT 
		FROM testDeleteCursor
		INTO @tableID
	END

	CLOSE testDeleteCursor
	DEALLOCATE testDeleteCursor


	--test insert
	DECLARE testInsertCursor CURSOR FOR
	SELECT TableID,NoOfRows
	FROM TestTables
	WHERE TestID=@testID
	ORDER BY Position DESC

	OPEN testInsertCursor

	FETCH NEXT 
	FROM testInsertCursor
	INTO @tableID,@nrRows

	WHILE @@FETCH_STATUS=0
	BEGIN
		SET @tableName=(SELECT Name 
		FROM Tables 
		WHERE TableID=@tableID)

		SET @startAt=GETDATE()
		--EXEC uspGenericInsert @tableName, @nrRows
		EXEC try_generic_insert @tableName, @nrRows
		SET @endAt=GETDATE()

		INSERT INTO TestRunTables VALUES (@testRunID,@tableID,@startAt,@endAt)

		FETCH NEXT 
		FROM testInsertCursor
		INTO @tableID,@nrRows
	END

	CLOSE testInsertCursor
	DEALLOCATE testInsertCursor

	-- test view
	DECLARE testViewCursor CURSOR FOR
	SELECT ViewID
	FROM TestViews
	WHERE TestID=@testID

	OPEN testViewCursor

	FETCH NEXT 
	FROM testViewCursor
	INTO @viewID

	WHILE @@FETCH_STATUS=0
	BEGIN
		SET @viewName=(SELECT Name 
		FROM Views 
		WHERE ViewID=@viewID)

		SET @startAt=GETDATE()
		EXEC uspSeeView @viewName
		SET @endAt=GETDATE()

		INSERT INTO TestRunViews VALUES (@testRunID,@viewID,@startAt,@endAt)

		FETCH NEXT 
		FROM testViewCursor
		INTO @viewID
	END

	CLOSE testViewCursor
	DEALLOCATE testViewCursor

	UPDATE TestRuns
	SET EndAt=GETDATE()
	WHERE TestRunID=@testRunID

END

exec mainTest 4

select * from ACCOMODATION
select * from DESTINATION
select * from Restaurant

select * from vAccInDest1
select * from vRestpid
select * from vAccDest


select * from TestRunTables
select * from TestRuns
select * from TestRunViews


DELETE FROM TestRuns
DELETE FROM TestRunTables
DELETE FROM TestRunViews
