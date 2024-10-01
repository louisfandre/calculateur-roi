from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def roi_form():
    if request.method == 'POST':
        # Récupération des données du formulaire
        name = request.form['name']
        company = request.form['company']
        email = request.form['email']
        phone = request.form['phone']

        # Récupération des données de l'entreprise
        num_clients = float(request.form['num_clients'])
        clv = float(request.form['clv'])
        retention_rate = float(request.form['retention_rate']) / 100  # Convertir en décimal
        conversion_rate = float(request.form['conversion_rate']) / 100
        current_budget = float(request.form['current_budget'])
        csat_score = float(request.form['csat_score'])
        num_complaints = float(request.form['num_complaints'])
        response_time = float(request.form['response_time'])
        fcr_rate = float(request.form['fcr_rate']) / 100
        churn_rate = float(request.form['churn_rate']) / 100

        # Calculs du ROI
        # 1. Amélioration de la rétention
        improved_retention_rate = retention_rate + 0.05  # Hypothèse de 5% d'augmentation
        additional_revenue_retention = num_clients * (improved_retention_rate - retention_rate) * clv

        # 2. Acquisition de nouveaux clients
        improved_conversion_rate = conversion_rate + 0.02  # Hypothèse de 2% d'augmentation
        new_leads = 1000  # Vous pouvez ajuster ce chiffre ou le demander dans le formulaire
        additional_revenue_acquisition = new_leads * (improved_conversion_rate - conversion_rate) * clv

        # 3. Réduction des coûts liés aux plaintes
        reduced_complaints = num_complaints * 0.20  # Hypothèse de 20% de réduction
        cost_per_complaint = 20  # Coût par plainte
        cost_savings_complaints = reduced_complaints * cost_per_complaint

        # 4. Réduction des coûts grâce à un meilleur FCR
        improved_fcr_rate = fcr_rate + 0.10  # Hypothèse de 10% d'amélioration
        time_saved = 50  # Heures économisées par mois
        agent_hourly_cost = 25  # Coût horaire des agents
        cost_savings_fcr = time_saved * agent_hourly_cost

        # Calcul final du ROI
        total_benefits = (additional_revenue_retention + additional_revenue_acquisition +
                          cost_savings_complaints + cost_savings_fcr)
        roi = ((total_benefits - current_budget) / current_budget) * 100

        # Préparer les données pour l'affichage
        result_data = {
            'name': name,
            'company': company,
            'additional_revenue_retention': additional_revenue_retention,
            'additional_revenue_acquisition': additional_revenue_acquisition,
            'cost_savings_complaints': cost_savings_complaints,
            'cost_savings_fcr': cost_savings_fcr,
            'total_benefits': total_benefits,
            'current_budget': current_budget,
            'roi': roi
        }

        # Afficher la page de résultats avec les données
        return render_template('result.html', data=result_data)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)