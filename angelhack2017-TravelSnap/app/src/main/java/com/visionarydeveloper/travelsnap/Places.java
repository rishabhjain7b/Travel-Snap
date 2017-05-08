package com.visionarydeveloper.travelsnap;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ListView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class Places extends Fragment {
    private static String JSON_DATA="[{\"name\": \"Savoy Suites\", \"vicinity\": \"Ansal Plaza Destination Point 1c, Institutional Area, Greater Noida\"}, {\"name\": \"Red Carpet Hotels Wedding and Birthday Party Hall\", \"vicinity\": \"Bs-31 Basai 201301, Sector 70, Noida\"}, {\"name\": \"Cytrus Hotels\", \"vicinity\": \"Next to RK Public School, Main Road, Mamura, 31-M, Mamura, Sector 66, Noida\"}, {\"name\": \"Commercial Tax Depatment Khnad-10 Noida UP\", \"vicinity\": \"Noida\"}, {\"name\": \"Shiv Narian Hotel\", \"vicinity\": \"Sector 102, Noida\"}, {\"name\": \"Sony Hotel\", \"vicinity\": \"Dadri Main Road, Sector - 106, Salarpur, Noida\"}, {\"name\": \"Lake savanna\", \"vicinity\": \"D-57, 2nd Floor, Noida\"}, {\"name\": \"SIR SYED APARTMENT\", \"vicinity\": \"Near Market,, Bhangel, Salarpur Khadar, Sector 110, Noida\"}, {\"name\": \"BLGC-SUPERB\", \"vicinity\": \"GH-004, Sector-110, Gautam Buddha Nagar, Noida\"}, {\"name\": \"BLGC-SUPERB\", \"vicinity\": \"gautam budh nagar, g h 004 sector 110 u p, Se\\u010d 2, Stara Cerkev\"}, {\"name\": \"Seru Hotel\", \"vicinity\": \"Dadri Main Road, Bhangel, Sector 102, Noida\"}, {\"name\": \"Haji Ji Ka Rehan Muslim Dhaba\", \"vicinity\": \"Dadri Main Road, Bhangel, Sector 102, Noida\"}, {\"name\": \"Haji Ji ka Rehan Muslim Hotel\", \"vicinity\": \"Dadri Main Road, Bhangel, Sector 102, Noida\"}, {\"name\": \"P.G In Noida\", \"vicinity\": \"c40 sector 44 noida u.p, Noida\"}, {\"name\": \"OYO Rooms 189 Noida Sector 110\", \"vicinity\": \"Gejha Road, Near Yatharth Wellness Hospital,Bhangel, Noida\"}, {\"name\": \"HOTEL NOIDA\", \"vicinity\": \"MAIN GEJHA ROAD, BHANGEL, NEAR SECTOR -110, Noida\"}, {\"name\": \"Swiggy Roommate\", \"vicinity\": \"201304, Goyal Colony, Salarpur Khadar, Sector 102, Noida\"}]";
    private DataAdapter dataAdapter;
    private ListView listView;
    private ArrayList<DataStructure> dataStructures;
     @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = (View) inflater.inflate(R.layout.fragment_places,
                container, false);
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
