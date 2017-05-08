package com.visionarydeveloper.travelsnap;

import android.app.Activity;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by gagan on 7/5/17.
 */

public class DataAdapter extends ArrayAdapter<DataStructure> {
    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        View gridView = convertView;
        if (gridView == null)
        {
            gridView = LayoutInflater.from(getContext()).inflate(R.layout.each_item, parent, false);
        }
        DataStructure currentAlphabet = getItem(position);

        TextView mainText = (TextView) gridView.findViewById(R.id.heading);
        mainText.setText(currentAlphabet.getMainName());

        TextView subText = (TextView) gridView.findViewById(R.id.sub_heading);
        subText.setText(currentAlphabet.getSubName());


        return gridView;
    }

    public DataAdapter(Activity context, ArrayList<DataStructure> ds){
        super(context,0,ds);
    }
}
