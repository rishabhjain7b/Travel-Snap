package com.visionarydeveloper.travelsnap;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ListView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;


public class Food extends Fragment {

    private static String JSON_DATA="[{\"name\": \"The Cake Experts\", \"vicinity\": \"Shop No-11, Block-A2, Sector-110, Noida\"}, {\"name\": \"Kamboj's Restaurant\", \"vicinity\": \"Hall No.1,39 A, Behind HDFC Bank, Sector 110, Noida\"}, {\"name\": \"kitchen65\", \"vicinity\": \"C-28, 2nd Floor, Sec 65, Noida\"}, {\"name\": \"DV's Chinese Kitchen\", \"vicinity\": \"Sector 110, Noida\"}, {\"name\": \"Kurrybox\", \"vicinity\": \"Noida\"}, {\"name\": \"Noida Bakery's - Himalaya Cakes Noida\", \"vicinity\": \"Gautam Buddha Nagar, Noida\"}, {\"name\": \"Super Cake Shop\", \"vicinity\": \"shop no G 5, expressway, near JP hospital sec 128, Sector - 106, Noida\"}, {\"name\": \"Flying Cakes\", \"vicinity\": \"Food Court, Ground Floor, Unitech Building, Sector 135, Noida\"}, {\"name\": \"The Chocolate Room\", \"vicinity\": \"GIP Mall, Sector -18, Sector - 106, Noida\"}, {\"name\": \"Flying Cakes\", \"vicinity\": \"Shop No 37 Kanchanjanga Market Sector 53, Noida\"}, {\"name\": \"Fresh Cake Pastry Shop\", \"vicinity\": \"A16/3, Sec - 71, Near Sai Baba mandir, Noida\"}, {\"name\": \"Chawla's 2 (Sec 50)\", \"vicinity\": \"1/54, B Block, Sectoer 50, Central Market, Noida\"}, {\"name\": \"The New Koyla Kitchen\", \"vicinity\": \"162,A, S.K. Behind Domino's, Sector 110, Noida\"}, {\"name\": \"Royal Eat\", \"vicinity\": \"Sector 110, Ravi Pradhan Market,Lane Next To Pizza Hut, Noida\"}, {\"name\": \"They\\u0938\\u0940\", \"vicinity\": \"A 2/11, Sector 110, Noida\"}, {\"name\": \"Travelling guru\", \"vicinity\": \"SDF-F-9-B, nSEZ\"}, {\"name\": \"Punjabi Dhaba\", \"vicinity\": \"Near Police Chowki Dadri Road, Bhangel Village, Bhangel, Sector 102, Noida\"}, {\"name\": \"BUY seLL SWARNIM VIHAR\", \"vicinity\": \"201304, Swarnim Vihar, Sector 82, Noida\"}, {\"name\": \"Moti Mahal Delux\", \"vicinity\": \"12-A,, Ashirwad Shopping Complex, Sector-104, Near Sector 110, Noida\"}, {\"name\": \"Munchin\", \"vicinity\": \"S160, 1st Floor, Sahara Mall, Opposite Central Arcade, Noida\"}]";
    private DataAdapter dataAdapter;
    private ListView listView;
    private ArrayList<DataStructure> dataStructures;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = (View) inflater.inflate(R.layout.fragment_food, container, false);
        dataStructures = new ArrayList<>();
        parseJson();
        listView = (ListView) view.findViewById(R.id.list);
        dataAdapter = new DataAdapter(getActivity(), dataStructures);
        listView.setAdapter(dataAdapter);
        return view ;
    }
    void parseJson(){
        try {
            JSONArray main = new JSONArray(JSON_DATA);
            for (int i = 0;i<main.length();i++){
                JSONObject name = main.getJSONObject(i);
                String nameStr = name.getString("name");
                String subnameStr = name.getString("vicinity");
                DataStructure dataStructure = new DataStructure(nameStr, subnameStr);
                dataStructures.add(dataStructure);
            }
        }
        catch (JSONException e){}
    }
}
