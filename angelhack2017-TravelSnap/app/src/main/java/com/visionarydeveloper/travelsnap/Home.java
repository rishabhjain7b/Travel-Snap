package com.visionarydeveloper.travelsnap;

import android.app.DownloadManager;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Environment;
import android.os.Handler;
import android.support.annotation.NonNull;
import android.support.v4.app.Fragment;
import android.util.Base64;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.Toast;
import android.widget.ViewFlipper;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.FirebaseApp;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;
import com.squareup.picasso.Picasso;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Hashtable;
import java.util.Map;

import static android.content.Context.MODE_PRIVATE;


public class Home extends Fragment {

    private Button location;
    private TrackGPS gps;
    double longitude;
    double latitude;

    private ProgressDialog progressDialog;
    private ImageView image;
    private Bitmap bitmap;

        private String UPLOAD_URL ="http://f2feead8.ngrok.io/api/zone/create.json";

    private String KEY_IMAGE = "image";
    private String KEY_NAME = "name";

    FirebaseAuth mAuth;

    public static final String Name = "imageKey";

    private int i = 0;


    private void signInAnonymously() {
        FirebaseApp.initializeApp(getActivity());
        mAuth = FirebaseAuth.getInstance();
        mAuth.signInAnonymously().addOnSuccessListener(getActivity(), new  OnSuccessListener<AuthResult>() {
            @Override
            public void onSuccess(AuthResult authResult) {
                // Create a reference to a file from a Google Cloud Storage URI
                StorageReference gsReference = FirebaseStorage.getInstance().getReferenceFromUrl(getResources().getString(R.string.url_to_teachers));
                Log.d("URL PRE",getResources().getString(R.string.url_to_teachers));
                gsReference.getDownloadUrl().addOnSuccessListener(new OnSuccessListener<Uri>() {
                    @Override
                    public void onSuccess(Uri uri) {
                        Log.d("URL AFTER",uri.toString());
                        Picasso.with(getContext()).load(uri.toString()).into(image);
                        downloadFile(uri.toString());
                        progressDialog.dismiss();
                    }
                });
            }
        })
                .addOnFailureListener(getActivity(), new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception exception) {
                    }
                });
    }

    public void downloadFile(String uRl) {
        File direct = new File(Environment.getExternalStorageDirectory()
                + "/TravelSnap");

        Log.d("PATH", direct.toString());
        boolean success=false;

        if (!direct.exists()) {
            success = direct.mkdir();
        }
        else{
            success = true;
        }
        if(success) {
            DownloadManager mgr = (DownloadManager) getActivity().getSystemService(Context.DOWNLOAD_SERVICE);

            Uri downloadUri = Uri.parse(uRl);
            DownloadManager.Request request = new DownloadManager.Request(downloadUri);

            int count = 0;
            SharedPreferences.Editor editor = getActivity().getPreferences(MODE_PRIVATE).edit();
            int defaultValue = getActivity().getPreferences(MODE_PRIVATE).getInt("count_key",count);
            ++defaultValue;
            getActivity().getPreferences(MODE_PRIVATE).edit().putInt("count_key",defaultValue).commit();
            count = getActivity().getPreferences(MODE_PRIVATE).getInt("count_key",count);
            Log.d("Shared Waali", count + "<--");

            request.setAllowedNetworkTypes(
                    DownloadManager.Request.NETWORK_WIFI
                            | DownloadManager.Request.NETWORK_MOBILE)
                    .setAllowedOverRoaming(false).setTitle("Demo")
                    .setDescription("Something useful. No, really.")
                    .setDestinationInExternalPublicDir("/TravelSnap", "test"+Integer.toString(count)+".jpg");

            Toast.makeText(getActivity(), "File : ", Toast.LENGTH_SHORT).show();
            mgr.enqueue(request);
        }
        else
            Toast.makeText(getContext(), "Bhai kuch diikkkaat hai", Toast.LENGTH_SHORT).show();
    }

    final Handler handlerGPS = new Handler();
    Runnable runnableGPS = new Runnable() {

        @Override
        public void run() {
            try{
                gps = new TrackGPS(getContext());


                if(gps.canGetLocation()){

                    longitude = gps.getLongitude();
                    latitude = gps .getLatitude();

                    SharedPreferences sharedPref = getActivity().getPreferences(Context.MODE_PRIVATE);
                    SharedPreferences.Editor editor = sharedPref.edit();
                    int defaultLat = (int)latitude;
                    editor.putInt("Latitude", (int)latitude);
                    int defaultLong = (int)longitude;
                    editor.putInt("Longitude", (int)longitude);
                    editor.apply();

                    Log.d("Something GPS", defaultLat + " , "+ defaultLong);
                    new Submitting().execute("Joey", Double.toString(latitude)+ "," + Double.toString(longitude) );

                    Toast.makeText(getContext(),"Longitude:"+Double.toString(longitude)+"\nLatitude:"+Double.toString(latitude),Toast.LENGTH_SHORT).show();
                }
                else
                {

                    gps.showSettingsAlert();
                }
            }
            catch (Exception e) {
                // TODO: handle exception
            }
            finally{
                //also call the same runnable to call it at regular interval
                handlerGPS.postDelayed(this, 30000);
            }
        }
    };

    final Handler handlerImg = new Handler();
    Runnable runnableImg = new Runnable() {

        @Override
        public void run() {
            try{
                progressDialog = new ProgressDialog(getActivity());
                progressDialog.setMessage("Loading data ....");
                progressDialog.setCanceledOnTouchOutside(false);
                progressDialog.show();
                signInAnonymously();
            }
            catch (Exception e) {
                // TODO: handle exception
            }
            finally{
                //also call the same runnable to call it at regular interval
                handlerImg.postDelayed(this, 10000);
            }
        }
    };

    ViewFlipper imageViewFlipper;
    Thread handlerSlideShowThread;
    Handler handlerSlideShow = new Handler();
    Runnable runnableSlideShow  = new Runnable() {
        public boolean stopThread = false;
        @Override
        public void run() {
            try {
                    if(!stopThread) {
                        imageViewFlipper.showNext();
                    }
            }
            catch (Exception e){}
            finally {
                handlerSlideShow.postDelayed(this, 2000);
            }
        }
    };

    private void setImagesToFlipper(ViewFlipper flipper, File sdcardPath) {
        if(!sdcardPath.exists()){
            sdcardPath.mkdir();
            Toast.makeText(getContext(), "Welcome new user, it'll take some time to fill up the space.", Toast.LENGTH_SHORT).show();
        }
        else {
            int imageCount = sdcardPath.listFiles().length;
            Log.d("PICTURES NUMNER", Integer.toString(imageCount));
            for (int count = 0; count < imageCount - 1; count++) {
                ImageView imageView = new ImageView(getContext());
                Bitmap bmp = BitmapFactory.decodeFile(sdcardPath.listFiles()[count].getAbsolutePath());
                Log.d("CHECK IT", bmp.toString());
                imageView.setImageBitmap(bmp);
                flipper.addView(imageView);
            }
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v= inflater.inflate(R.layout.fragment_home, container, false);

        imageViewFlipper = (ViewFlipper) v.findViewById(R.id.main_flipper);

        File direct = new File(Environment.getExternalStorageDirectory() + "/TravelSnap");

        setImagesToFlipper(imageViewFlipper, direct);

        handlerSlideShowThread = new Thread(runnableSlideShow);
        handlerSlideShowThread.start();
//        location = (Button) v.findViewById(R.id.location);

        new Thread(runnableGPS).start();
//        location.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//
//                gps = new TrackGPS(getContext());
//
//
//                if(gps.canGetLocation()){
//
//
//                    longitude = gps.getLongitude();
//                    latitude = gps .getLatitude();
//                new Submitting().execute("Testdata", Double.toString(longitude) + "," + Double.toString(latitude));
//
//                    Toast.makeText(getContext(),"Longitude:"+Double.toString(longitude)+"\nLatitude:"+Double.toString(latitude),Toast.LENGTH_SHORT).show();
//                }
//                else
//                {
//
//                    gps.showSettingsAlert();
//                }
//
//            }
//        });

//        location.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                uploadImage();
//                new Submitting().execute("Testdata","IMAGESIDE");
//                progressDialog = new ProgressDialog(getActivity());
//                progressDialog.setMessage("Loading data ....");
//                progressDialog.setCanceledOnTouchOutside(false);
//                progressDialog.show();
//                signInAnonymously();
//            }
//        });
        return v;
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        handlerSlideShowThread.interrupt();
    }

    private class Submitting extends AsyncTask<String,Void,String> {
        ProgressDialog progress;
        @Override
        protected void onPreExecute() {
            super.onPreExecute();
            progress=new ProgressDialog(getActivity());
            progress.setMessage("Registring....");
            progress.show();
        }

        @Override
        protected String doInBackground(String... string) {
            String title=string[0];
            String position=string[1];
            String response="";
            JSONObject jsonObject=new JSONObject();
            try {

                jsonObject.put("name",title);
                jsonObject.put("position", position);
                URL url = new URL(UPLOAD_URL); //Enter URL here
                HttpURLConnection httpURLConnection = (HttpURLConnection)url.openConnection();
                httpURLConnection.setDoOutput(true);
                httpURLConnection.setRequestMethod("POST"); // here you are telling that it is a POST request, which can be changed into "PUT", "GET", "DELETE" etc.
                httpURLConnection.setRequestProperty("Content-Type", "application/json"); // here you are setting the `Content-Type` for the data you are sending which is `application/json`
                httpURLConnection.connect();
                DataOutputStream wr = new DataOutputStream(httpURLConnection.getOutputStream());
                wr.writeBytes(jsonObject.toString());
                wr.flush();
                wr.close();
                InputStream inputStream=httpURLConnection.getInputStream();
                if(inputStream==null){
                    Log.e("Manual","input stream is null");
                }
                StringBuffer buffer=new StringBuffer();
                String line="";
                BufferedReader bufferedReader=new BufferedReader(new InputStreamReader(inputStream));
                while((line=bufferedReader.readLine())!=null){
                    buffer.append(line+"\n");
                }
                response=buffer.toString();
                Log.d("SubmitActivity",response);
            } catch (Exception e) {
                e.printStackTrace();
            }
            return response;
        }

        @Override
        protected void onPostExecute(String res) {
            super.onPostExecute(res);
            String r=res.trim();
            Log.d("TAG","scaaaaaaaaaaaaaaaaaaa"+r);
            if(!(r.equals(""))){
                Log.d("TAG","sca"+r);
                Toast.makeText(getActivity(),"User Succsessfully Registered!!",Toast.LENGTH_SHORT).show();
                progress.cancel();
            }

        }
    }
}