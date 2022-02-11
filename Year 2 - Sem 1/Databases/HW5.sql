--tb
CREATE TABLE SERVICES_PROVIDER
(
	pId INT PRIMARY KEY,
	nr_employees int,
	provider_name VARCHAR(50)
)


--ta, surface unique
CREATE TABLE DESTINATION
	(destId INT PRIMARY KEY,
	 surface int,
	 destination_name VARCHAR(50)
	)

ALTER TABLE destination
ADD CONSTRAINT Unique_surface UNIQUE (surface)

--tc
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

go
CREATE OR ALTER PROCEDURE uspGenericInsert @tableName VARCHAR(50), @nrRows INT AS
BEGIN

	DECLARE @i INT
	SET @i = 1


	declare @dest_name varchar(50)
	declare @surface int

	declare @AId int
	declare @acc_name varchar(50)
	declare @acc_type varchar(50)
	declare @destId int
	declare @pId int

	
	declare @provider_name varchar(50)
	declare @nr_employees int

	WHILE @i <= @nrRows
		BEGIN
			if @tableName='Destination'
			begin
					set @destId=@i
					set @dest_name='destination'+ convert(varchar(50), @destId)
					set @surface=@i*1000 + FLOOR(rand()*124)
					insert into DESTINATION(destId,surface,destination_name) values (@destId,@surface,@dest_name)
			end

			if @tableName='Accomodation'
			begin
					set @AId=@i
					set @acc_name='acc name'+convert(varchar(50), @i)
					set @acc_type='acc type'+convert(varchar(50), @i)
					set @destId=@i%10+1
					set @pId=@i
					insert into ACCOMODATION(AId,acc_name,acc_type,destId,pId) values (@AId,@acc_name,@acc_type,@destId, @pId)
			end

			if @tableName='Services_Provider'
			begin
					set @pId=@i
					set @provider_name='provider '+convert(varchar(50), @i)
					set @nr_employees=FLOOR(rand()*124)
					insert into SERVICES_PROVIDER(pId,nr_employees,provider_name) values(@pId, @nr_employees, @provider_name)

			end

			SET @i = @i + 1

		END
END

exec uspGenericInsert accomodation,100
select * from DESTINATION
select * from ACCOMODATION
select * from SERVICES_PROVIDER


--Index scan: Touch all rows but certain columns.
--Index seek: Touch certain rows and certain columns.

--a. clustered index scan
select * 
from DESTINATION
order by destId desc


--a.clustered index seek
select * 
from DESTINATION
where destId > 3

--a.nonclustered index scan

select surface
from DESTINATION


--a.nonclustered index seek
select surface
from DESTINATION
where surface>5000 and surface<12300

--a.key lookup
select *
from DESTINATION
where surface=5631


--b.
--estimated subtree cost (no index) : 0,003392

select * 
from SERVICES_PROVIDER
where nr_employees = 115

--estimated subtree cost (with index) : 0,0032831
drop index if exists nonclusteredIndexSP on services_provider
create nonclustered index nonclusteredIndexSP on services_provider(nr_employees) include (provider_name)

select * 
from SERVICES_PROVIDER
where nr_employees = 115

--after the creation of the index we go from a clustered index scan to a nonclustered index seek, which is more efficient 

--c. Create a view that joins at least 2 tables.
go
create or alter view accinDest
as
	select S.pId, S.provider_name, A.AId, A.acc_name, D.destId, D.destination_name, d.surface
	from SERVICES_PROVIDER s inner join ACCOMODATION a on a.pid=s.pId inner join
	DESTINATION d on d.destId=a.destId
	where d.surface < 7888

-- estimated subtree cost : 0.03727
select * from accinDest

drop index nonClusteredIndexAcc on Accomodation
create nonclustered index nonClusteredIndexAcc on accomodation(destid,pid)  

-- estimated subtree cost : 0.03700
select * from accinDest
