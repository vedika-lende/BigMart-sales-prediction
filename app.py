from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)


# =====================================================
# LOAD MODEL AND SCALER
# =====================================================

with open("bigmart_knn_model.pkl", "rb") as file:
    saved_data = pickle.load(file)

# Your pickle contains:
# {
#     "model": KNeighborsRegressor,
#     "scaler": MinMaxScaler
# }

model = saved_data["model"]
scaler = saved_data["scaler"]


# =====================================================
# HOME PAGE
# =====================================================

@app.route("/")
def home():
    return render_template("index.html")


# =====================================================
# PREDICTION
# =====================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # -------------------------------------------------
        # Get values from form
        # -------------------------------------------------

        item_weight = float(request.form["item_weight"])

        item_fat_content = int(
            request.form["item_fat_content"]
        )

        item_visibility = float(
            request.form["item_visibility"]
        )

        item_mrp = float(
            request.form["item_mrp"]
        )

        outlet_size = int(
            request.form["outlet_size"]
        )

        outlet_location_type = int(
            request.form["outlet_location_type"]
        )

        outlet_establishment_year = int(
            request.form["outlet_establishment_year"]
        )

        item_type = request.form["item_type"]

        outlet_identifier = request.form[
            "outlet_identifier"
        ]

        outlet_type = request.form[
            "outlet_type"
        ]


        # -------------------------------------------------
        # Create basic input dataframe
        # -------------------------------------------------

        input_data = pd.DataFrame({

            "Item_Weight": [item_weight],

            "Item_Fat_Content": [
                item_fat_content
            ],

            "Item_Visibility": [
                item_visibility
            ],

            "Item_MRP": [
                item_mrp
            ],

            "Outlet_Establishment_Year": [
                outlet_establishment_year
            ],

            "Outlet_Size": [
                outlet_size
            ],

            "Outlet_Location_Type": [
                outlet_location_type
            ]

        })


        # =================================================
        # ITEM TYPE DUMMY COLUMNS
        # =================================================

        item_type_columns = [

            "Item_Type_Breads",

            "Item_Type_Breakfast",

            "Item_Type_Canned",

            "Item_Type_Dairy",

            "Item_Type_Frozen Foods",

            "Item_Type_Fruits and Vegetables",

            "Item_Type_Hard Drinks",

            "Item_Type_Health and Hygiene",

            "Item_Type_Household",

            "Item_Type_Meat",

            "Item_Type_Others",

            "Item_Type_Seafood",

            "Item_Type_Snack Foods",

            "Item_Type_Soft Drinks",

            "Item_Type_Starchy Foods"

        ]


        # Create all columns with 0

        for col in item_type_columns:

            input_data[col] = 0


        # Set selected item type to 1

        selected_item_col = (
            "Item_Type_" + item_type
        )


        if selected_item_col in input_data.columns:

            input_data[selected_item_col] = 1


        # =================================================
        # OUTLET IDENTIFIER DUMMY COLUMNS
        # =================================================

        outlet_columns = [

            "Outlet_Identifier_OUT010",

            "Outlet_Identifier_OUT013",

            "Outlet_Identifier_OUT017",

            "Outlet_Identifier_OUT018",

            "Outlet_Identifier_OUT019",

            "Outlet_Identifier_OUT027",

            "Outlet_Identifier_OUT035",

            "Outlet_Identifier_OUT045",

            "Outlet_Identifier_OUT046",

            "Outlet_Identifier_OUT049"

        ]


        # Create all columns with 0

        for col in outlet_columns:

            input_data[col] = 0


        # Set selected outlet to 1

        selected_outlet = (
            "Outlet_Identifier_"
            + outlet_identifier
        )


        if selected_outlet in input_data.columns:

            input_data[selected_outlet] = 1


        # =================================================
        # OUTLET TYPE DUMMY COLUMNS
        # =================================================

        outlet_type_columns = [

            "Outlet_Type_Supermarket Type1",

            "Outlet_Type_Supermarket Type2",

            "Outlet_Type_Supermarket Type3"

        ]


        # Create all columns with 0

        for col in outlet_type_columns:

            input_data[col] = 0


        # Set selected outlet type to 1

        selected_type = (
            "Outlet_Type_" + outlet_type
        )


        if selected_type in input_data.columns:

            input_data[selected_type] = 1


        # =================================================
        # ARRANGE COLUMNS IN TRAINING ORDER
        # =================================================

        training_columns = (
            model.feature_names_in_
        )


        input_data = input_data.reindex(

            columns=training_columns,

            fill_value=0

        )


        # =================================================
        # SCALE INPUT DATA
        # =================================================

        scaled_input = scaler.transform(
            input_data
        )


        # =================================================
        # MAKE PREDICTION
        # =================================================

        prediction = model.predict(
            scaled_input
        )[0]


        # =================================================
        # RETURN RESULT
        # =================================================

        return render_template(

            "index.html",

            prediction=round(
                prediction,
                2
            )

        )


    except Exception as e:

        return f"""
        <h2>Prediction Error</h2>
        <p>{str(e)}</p>
        <br>
        <a href="/">Go Back</a>
        """


# =====================================================
# RUN FLASK
# =====================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )