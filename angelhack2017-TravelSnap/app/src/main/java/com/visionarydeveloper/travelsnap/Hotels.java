package com.visionarydeveloper.travelsnap;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;


public class Hotels extends Fragment {
    private static String JSON_DATA = "[{\"name\": \"Sarai Hotel\", \"vicinity\": \"5-A Canal Bank Road, Lahore\"}, {\"name\": \"atomic energy mineral center\", \"vicinity\": \"Lahore\"}, {\"name\": \"Block EE - state life housing phase 22\", \"vicinity\": \"Lahore\"}, {\"name\": \"Naulakha hotel\", \"vicinity\": \"132 Allama Iqbal Road, Lahore\"}, {\"name\": \"Main Rahman Park\", \"vicinity\": \"Lahore\"}, {\"name\": \"Midland Hotel\", \"vicinity\": \"Street 1, Lahore\"}, {\"name\": \"Al Sheikh Hotel Allama Iqbal Road Mustafa Abad Lahore\", \"vicinity\": \"179 Allama Iqbal Rd, Mustafa Abad, Lahore\"}, {\"name\": \"Mall View Hotel\", \"vicinity\": \"Lahore\"}, {\"name\": \"Executives Inn\", \"vicinity\": \"Canal Bank Road, Lahore\"}, {\"name\": \"Shimla Hill Hotel Lahore\", \"vicinity\": \"Davis Road, Lahore\"}, {\"name\": \"Bnu hostel\", \"vicinity\": \"Lahore\"}], \"poi\": [{\"name\": \"Trendies.Pk Online Shopping in Pakistan\", \"vicinity\": \"Online Store Bases in, Lahore\"}, {\"name\": \"City Shopping Centet\", \"vicinity\": \"Lahore\"}, {\"name\": \"Zaman Park\", \"vicinity\": \"Lahore\"}, {\"name\": \"Miraan Arts\", \"vicinity\": \"Lahore\"}, {\"name\": \"AHMED PLAZA LAHORE\", \"vicinity\": \"Lahore\"}, {\"name\": \"The Lancaster\", \"vicinity\": \"Sunderdas Road, Lahore\"}, {\"name\": \"Bobby Sports\", \"vicinity\": \"2 Allama Iqbal Road, Lahore\"}, {\"name\": \"f.a Traders\", \"vicinity\": \"mustafa abad, Street 35, Lahore\"}, {\"name\": \"City Shopping Center\", \"vicinity\": \"Street Number: 32, Lahore\"}, {\"name\": \"Al Sheikh Mobiles\", \"vicinity\": \"Mian Mir Darbar Road, Lahore\"}, {\"name\": \"Saman Arcade\", \"vicinity\": \"J, 3 Street 1, Lahore\"}, {\"name\": \"Darbar Hazrat Nathy Pak\", \"vicinity\": \"Lahore\"}, {\"name\": \"Mobi World\", \"vicinity\": \"Shop No.14-15 Lahore Tower Barkat Market,Near Gourmet Bakers, Lahore\"}, {\"name\": \"Moono squash complex\", \"vicinity\": \"Lahore\"}]", UPLOAD_URL;
    private DataAdapter dataAdapter;
    private ListView listView;
    private ArrayList<DataStructure> dataStructures;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        dataStructures = new ArrayList<>();
//        if (JSON_DATA == null){
//            volley();
//        }
        View view = (View) inflater.inflate(R.layout.fragment_hotels, container, false);
        listView = (ListView) view.findViewById(R.id.list);
                                parseJson();

        dataAdapter = new DataAdapter(getActivity(), dataStructures);
        listView.setAdapter(dataAdapter);
        return view ;
    }
    void parseJson(){
        try {
            JSONArray main= new JSONArray(JSON_DATA);
//            JSONArray hotels = main.getJSONArray("hotel");
            for (int i = 0;i<main.length();i++){
                JSONObject name = main.getJSONObject(i);
                String nameStr = name.getString("name");
                String subnameStr = name.getString("vicinity");
                Log.d("JSON", nameStr + " " + subnameStr);
                DataStructure dataStructure = new DataStructure(nameStr, subnameStr);
                dataStructures.add(dataStructure);
                Log.d("JSON ke badd", Integer.toString(dataStructures.size()));

            }
        }
        catch (JSONException e){}
    }
    void volley(){
        SharedPreferences sharedPref = getActivity().getPreferences(Context.MODE_PRIVATE);
        int defaultLat = sharedPref.getInt("Latitude",0);
        int defaultLong = sharedPref.getInt("Longitude",0);
        UPLOAD_URL ="http://f2feead8.ngrok.io/recommend/" + defaultLat +"/" + defaultLong;
        Log.d("Request 1", UPLOAD_URL);
        // Instantiate the RequestQueue.
        RequestQueue queue = Volley.newRequestQueue(getContext());

        // Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.GET, UPLOAD_URL,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        JSON_DATA = response;
                        Log.d("RESPONSE VOLLEY", JSON_DATA);
//                        parseJson();

                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Toast.makeText(getContext(), "Data not loaded. Try again in some time.", Toast.LENGTH_SHORT).show();
            }
        });
        // Add the request to the RequestQueue.
        queue.add(stringRequest);
        Toast.makeText(getContext(), defaultLat + " , " + defaultLong, Toast.LENGTH_SHORT).show();
    }
}
