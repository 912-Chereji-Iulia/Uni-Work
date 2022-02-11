--insert, update, delete statements
-- multiple queries
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
ADD destId INT
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
ADD pId INT
CONSTRAINT FK_TRANSPORT_pId
	FOREIGN KEY (pId)
	REFERENCES  SERVICES_PROVIDER(pId)

CREATE TABLE TRANSPORT_DESTINATION
	(tId INT REFERENCES TRANSPORT(tID),
	 destId INT REFERENCES DESTINATION(destId),
	 PRIMARY KEY(tId,destId)

)


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

/* QUERIES*/

/* union operator - OR */
/* find the name and type of transport that go to Paris OR Rome */
select DISTINCT T.tr_name, T.tr_type 
FROM TRANSPORT T, TRANSPORT_DESTINATION TD, DESTINATION D
WHERE TD.tId=T.tId AND TD.destId = D.destId AND
	(D.destination_name = 'Paris' OR D.destination_name = 'Rome')

select DISTINCT C.FirstName, C.LastName
from CLIENT C, BILL_CLIENT BC, BILL B
where C.CNP=BC.CNP AND BC.BillId=B.BillId and (B.ValueofBill>100 or B.DateofBill='08-02-2002')

/* union operator - UNION - accomodation in Paris or LA*/
SELECT  A.acc_name
FROM ACCOMODATION A
WHERE A.destId=1
UNION 
SELECT A1.acc_name
FROM ACCOMODATION A1
WHERE A1.destId=2

/* intersection operation - IN - name of persons who paid for bill with id 2*/
select C.LastName + ' '+C.FirstName as full_name
from CLIENT C
where C.CNP IN
(  select BC.CNP
	from BILL_CLIENT BC
	WHERE BC.BillId = 2
)

/* intersection operation - INTERSECT - transport that goes to Paris and Rome*/
SELECT T.tr_name
FROM TRANSPORT T,TRANSPORT_DESTINATION TD, DESTINATION D
WHERE T.tId=TD.tId AND TD.destId=D.destId AND D.destination_name='Paris'
INTERSECT
SELECT T1.tr_name
FROM TRANSPORT T1,TRANSPORT_DESTINATION TD1, DESTINATION D1
WHERE T1.tId=TD1.tId AND TD1.destId=D1.destId AND D1.destination_name='Rome'

/*difference operation - NOT IN */
/* ids of offers that have the dest Paris but not Rome */

select O.OfferId
FROM OFFER O, OFFER_DESTINATION OD, DESTINATION D
WHERE OD.OfferId=O.OfferId AND OD.destId = D.destId AND D.destination_name = 'Paris' AND
d.destId NOT IN ( SELECT OD1.destID
				FROM OFFER_DESTINATION OD1, DESTINATION D1
				WHERE OD1.destId = D1.destId AND D1.destination_name = 'Rome')

/*difference operation - EXCEPT - all offers that don t have Paris as destination */
SELECT *
FROM OFFER O,OFFER_DESTINATION OD, DESTINATION D
WHERE O.OfferId=OD.OfferId AND OD.destId=D.destId
EXCEPT
SELECT *
FROM OFFER O1,OFFER_DESTINATION OD1, DESTINATION D1
WHERE O1.OfferId=OD1.OfferId AND OD1.destId=D1.destId AND D1.destination_name='Paris'


/*find the ids of offers that  have Paris as destination - EXISTS*/
select O.OfferId
from OFFER O
where EXISTS ( select *
				from OFFER_DESTINATION OD
				where OD.destId = 1 AND O.OfferId=OD.OfferId
				)

/*find the names of employees that work in sales department - EXISTS */
select top 3 E.EmployeeId, E.FirstName, E.LastName, E.Salary
from EMPLOYEE E
where EXISTS ( select *
				from DEPARTMENT D
				where D.DepartmentName='sales' AND D.DepartmentId=E.DepartmentId 
				)
order by E.Salary desc

/*find the names of accomodations that are provided by Service provider with id 1 - EXISTS */
select A.acc_name,S1.provider_name
from ACCOMODATION A, SERVICES_PROVIDER S1
where EXISTS ( select *
				from SERVICES_PROVIDER S
				where S.pId=1 AND S.pId=A.pId and S1.pId=S.pId
				)

/* find the names of the accomodations that are in Paris - IN operator */
select A.acc_name
from ACCOMODATION A
WHERE A.destId in 
	(select D.destId
	from DESTINATION D
	where D.destination_name='Paris'
	)

/* find the names of the transports that go to Rome - IN operator*/
select T.tr_name
from TRANSPORT T
WHERE T.tId in 
	(select TD.tId
	from TRANSPORT_DESTINATION TD
	where TD.destId in 
		(
		select D.destId
		from DESTINATION D
		where D.destination_name='Rome'
		)

	)


/* find the hotels name and transport name; include the destinations name -- INNER JOIN */

select A.acc_name, T.tr_name, D.destination_name
from ACCOMODATION A INNER JOIN DESTINATION D ON A.destId=D.destId
INNER JOIN TRANSPORT_DESTINATION TD ON TD.destId=D.destId
INNER JOIN TRANSPORT T ON T.tId=TD.tId

/* clients that paid to go to Paris - 2 many to many */
select distinct C.FirstName, C.LastName
from CLIENT C INNER JOIN BILL_CLIENT BC ON BC.CNP= C.CNP 
INNER JOIN BILL B ON B.BillId=BC.BillId  
INNER JOIN OFFER O ON O.OfferId=B.OfferId
INNER JOIN OFFER_DESTINATION OD on Od.OfferId=O.OfferId
INNER JOIN DESTINATION D on OD.destId=D.destId and D.destination_name='Paris'



/* subquery in FROM clause - accomodations in destinations with id < 5 and not 2,3 */
select A.*
from ACCOMODATION A INNER JOIN 
	( select *
	from DESTINATION D
	where D.destId <5 and D.destId not in (2,3)
	) d
ON d.destId=A.destId
order by A.destId

/* subquery in FROM clause - employees who are getting offers from provider WIZZAIR or Fany Transport or Deluxe Ships */
select distinct E.*, salary_increased= E.Salary + 100 
from EMPLOYEE E INNER JOIN 
	( select *
	from SERVICES_PROVIDER S
	where S.provider_name='WizzAir' or  S.provider_name='Fany Transport' or S.provider_name='Deluxe Ships'
	) d
ON d.EmployeeId=E.EmployeeId


/* right join -employees including departments and the branches with no employee assigned */
select E.FirstName, E.LastName, E.Job, D.DepartmentId,D.DepartmentName,B.BranchId,B.City
from EMPLOYEE E
RIGHT OUTER JOIN DEPARTMENT D on d.DepartmentId=E.DepartmentId 
RIGHT OUTER JOIN BRANCH B on B.BranchId=D.BranchId

/*full outer join*/
select C.FirstName,C.LastName, B.BillId, O.OfferId
from CLIENT C
full OUTER JOIN BILL_CLIENT BC on BC.CNP=C.CNP
full outer join BILL B on B.BillId=BC.BillId
full outer join OFFER O on o.OfferId=B.OfferID

/* left outer join- providers name and the transport provided by them, also providers with no transport */
select S.provider_name, T.tr_name
from SERVICES_PROVIDER S
left outer join TRANSPORT T on t.pId=S.pId

/* group by - employees and the nr of bills emitted by them */
select top 3 E.EmployeeId, COUNT(*) as bills_emitted
from EMPLOYEE E, BILL B
where E.EmployeeId=B.EmployeeID
group by E.EmployeeId
order by bills_emitted

/* id of employees with nr of bills emitted greater then the average */
select E.EmployeeId
from EMPLOYEE E, BILL B
where B.EmployeeID=E.EmployeeId
group by E.EmployeeId
having COUNT(*) >
(
	select AVG(bills_emitted) as Average_nr_bills
	from (
		select E.EmployeeId, COUNT(*) as bills_emitted
		from EMPLOYEE E, BILL B
		where E.EmployeeId=B.EmployeeID
		group by E.EmployeeId
	) t
)



/* total value of bills for the offer with id 1 or 2 - group by */
select SUM(B.ValueofBill) As Sum_of_bills, sum_without_taxes=SUM(B.ValueofBill)-50
from BILL B
group by B.OfferID
having B.OfferID IN (1,2)


/* id most productive employee -group by*/

select E.EmployeeId
from EMPLOYEE E, BILL B
where B.EmployeeID=E.EmployeeId
group by E.EmployeeId
having COUNT(*) =
(
select MAX(bills_emitted) as Min_nr_bills
from(
	select E.EmployeeId, COUNT(*) as bills_emitted
	from EMPLOYEE E, BILL B
	where E.EmployeeId=B.EmployeeID
	group by E.EmployeeId
) t

)

/* the least popular destinations based on the nr of bills emitted  */
select D.destination_name
from DESTINATION D
where D.destId IN(
	select OD.destId
	from OFFER_DESTINATION OD
	where OD.OfferId In (
		select O.OfferId
		from OFFER O
		where O.OfferId IN(
			select B.OfferId
			from BILL B
			group by B.OfferId
			HAVING Count(*)=
				(
				select MIN(bills_for_offer) as MIN_NR_OFFERS
				from(
					select COUNT(*) as bills_for_offer
					from BILL B
					group by B.OfferID
				) t
				)
		)
	)
)

/*ANY - names of employees whose salary is equal to the salary of some employee Ioana */
select E.FirstName, E.LastName, E.Salary
from EMPLOYEE E
where E.Salary= ANY
	( select E1.Salary
	from EMPLOYEE E1
	where E1.FirstName='Ioana' 
	)
/* rewrite*/
select E.FirstName, E.LastName, E.Salary
from EMPLOYEE E
where E.Salary IN
	( select E1.Salary
	from EMPLOYEE E1
	where E1.FirstName='Ioana' 
	)

/*bill ids whose value is greater then the date of bill 08-02-2021 */
select B.BillId, B.ValueofBill
from BILL B
where B.ValueofBill> ANY
	(
	select B1.ValueofBill
	from BILL B1
	where B1.DateofBill='08-02-2021'
	)

/* rewrite aggregation */

select B.BillId, B.ValueofBill
from BILL B
where B.ValueofBill>
	(
	select MIN(B1.ValueofBill)
	from BILL B1
	where B1.DateofBill='08-02-2021'
	)


/* ALL - names of employees whose salary is smaller then the salary of every employee with first name Iulia */

select E.FirstName +' '+ E.LastName as FullName, E.Salary
from EMPLOYEE E
where E.Salary < ALL
	( select E1.Salary
	from EMPLOYEE E1
	where E1.FirstName='Iulia' 
	)

/*rewrite */
select  E.FirstName +' '+ E.LastName as FullName, E.Salary
from EMPLOYEE E
where E.Salary < 
	( select MIN(E1.Salary) 
	from EMPLOYEE E1
	where E1.FirstName='Iulia' 
	)


/* bill ids of bills that don t have as offer the one with id 2 */
select B.BillId, B.ValueofBill, B.OfferID 
from BILL B
where B.BillId <> ALL
	(
	select B1.BillId
	from BILL B1, OFFER O
	where B1.OfferID= O.OfferId and O.OfferId = 2
	)
order by B.ValueofBill desc

/* rewrite*/
select B.BillId, B.ValueofBill, B.OfferID 
from BILL B
where B.BillId NOT IN
	(
	select B1.BillId
	from BILL B1, OFFER O
	where B1.OfferID= O.OfferId and O.OfferId = 2
	)
order by B.ValueofBill desc
