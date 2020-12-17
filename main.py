from flask import Flask,render_template,request

app =Flask(__name__)


@app.route("/",methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':    
        creditcardnumber = request.form.get('creditcardnumber')
        print("creditcardnumber : ",creditcardnumber)
        cardholder = request.form['cardholder']
        print("cardholder : ",cardholder)
        expirationdate = request.form['expirationdate']
        print("expirationdate : ",expirationdate)
        securitycode = request.form['securitycode']
        print("securitycode : ",securitycode)
        amount = request.form['amount']
        print("amount : ",amount)
        amount=int(amount)
        print("type",type(amount))
        if(amount <= 20):
            print("in less than 20")
            return '''<h3>CheapPaymentGateway</h3> '''
        elif(amount in range(21,501)):
            print("in range")
            return '''<h3>ExpensivePaymentGateway</h3> '''
        elif(amount > 500):
            return '''<h3>PremiumPaymentGateway</h3> '''
        else:
            return "Try after some time"

    return render_template("home_page.html")

if __name__=="__main__":
    app.run(host='localhost',port=3000,debug=True)