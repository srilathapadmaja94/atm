from flask import Flask,render_template,request,redirect
import datetime

app = Flask(__name__)
global database,l,amount,x
database={"padmaja":["8686","3053",[6000]]}
l=[]

@app.route("/",methods=['GET','POST'])
def index():
	username = request.form.get('username')
	password = request.form.get('password')
	for i,j in database.items():
		if username == i and password == j[0]:
			return render_template('layout.html')
		
	return render_template("welcomepage.html")
	
@app.route("/withdraw",methods=['GET','POST'])
def withdraw():
	dt= datetime.datetime.now()
	x = dt.strftime("%Y-%m-%d %H:%M:%S")
	withdrawamount = request.form.get('withdraw_amount')
	Atmpin = request.form.get('Atm_pin')
	for password, Ac_num, amount in database.values():
		print(password)
		print(Atmpin)
		if Atmpin == password:
			if amount[-1]>=int(withdrawamount):
				an = amount[-1] - int(withdrawamount)
				amount.append(an)
				b = "Debit", "-"+f"{int(withdrawamount)}",f"{x}"
				l.append(b)
				return render_template("msg.html",database=database,l=l,x=x,msg = "Amount {} is debited successfully".format(withdrawamount))
			return render_template("withdrawfail.html", database=database, l=l,x=x)
	return render_template("withdraw.html",database=database,l=l)

@app.route("/deposit",methods=['GET','POST'])
def deposit():
	dt= datetime.datetime.now()
	x = dt.strftime("%Y-%m-%d %H:%M:%S")		
	Depositamount = request.form.get('Deposit_amount')
	Acnum1 = request.form.get('Ac_num')
	for password, Acnum, amount in database.values():
		if Acnum1 == Acnum:
			an = amount[-1] + int(Depositamount)
			amount.append(an)
			b = "Credit", "+"+f"{int(Depositamount)}",f"{x}"
			l.append(b)
			return render_template("msg.html",database=database,l=l,x=x,msg = "Amount {} is credited successfully".format(Depositamount))
	return render_template("deposit.html",database=database,l=l)

@app.route("/ministatement",methods=['GET','POST'])
def ministatement():
	dt= datetime.datetime.now()
	x = dt.strftime("%Y-%m-%d %H:%M:%S")
	for password, Ac_num, amount in database.values():
		return render_template("ministatement.html",database=database,l=l,amount=amount,x=x)
	return render_template("ministatement.html",l=l, amount = amount, database= database)
	

@app.route("/exit",methods=['GET','POST'])
def exit():
    return render_template("layout.html")



if __name__ == '__main__':
	app.run(debug=True,port=5002)