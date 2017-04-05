package com.example.kiran.calculater;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Environment;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.GridView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.File;
import java.io.FileOutputStream;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemClickListener{

    EditText in;
    TextView tv;
    String re="0";
    File file;
    int trigpos;
    ArrayList<Double> number =  new ArrayList<Double>();
    ArrayList<Integer> operator = new ArrayList<Integer>();
    GridView gridview;
    static double result=0;
    int pos=-1;
    public static String[] numpad = new String[]{"7","8","9","/",
            "4","5","6","*",
            "1","2","3","+",
            "Recall","0","=",
            "sin","cos","tan","clear"};
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        gridview = (GridView)findViewById(R.id.gridView);
        // in = (EditText)findViewById(R.id.editText);
        tv = (TextView)findViewById(R.id.txtresult);
        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,android.R.layout.simple_list_item_1,numpad);
        gridview.setAdapter(adapter);
        gridview.setOnItemClickListener(this);
    }

    public void onItemClick(AdapterView<?> parent, View v,int position, long id)
    {
        int temp1;
        String temp = ((TextView) v).getText().toString();
        if(position == 3 || position == 7 || position == 11 )
        {
            number.add(result);
            re="0";
            pos = position;
            operator.add(pos);
        }
        else if(position==12)
        {
            SharedPreferences sharedpreference1 = PreferenceManager.getDefaultSharedPreferences(this);
            String getdatafrompreference = sharedpreference1.getString("result","10");
            tv.setText(getdatafrompreference);
        }
        else if(position==18)
        {
            tv.setText("");
            result=0;
            re = "0";
            pos=-1;
            number=null;
            operator=null;
        }
        else if(position==15 || position==16||position==17)
        {
            trigpos = position;
            operator.add(trigpos);
        }
        else
        {
            if(position==14)
            {
                number.add(result);
                int j=0;
                result = number.get(0);
                double tempe = result /180.0*(22/7.0);
                if(trigpos==15)
                 {
                result = Math.sin(tempe);
                }
                else if(trigpos==16)
                {
                    result = Math.cos(tempe);
                }
                else if(trigpos==17){
                    result = Math.tan(tempe);
                }
                for(int i=1;i<number.size();i++)
                {
                    int op = operator.get(j);
                    j++;
                    if(op==11)
                    {
                        result = result + number.get(i);
                    }
                    else if(op==7)
                    {
                        result = result * number.get(i);
                    }
                    else if(op==3)
                    {
                        result = result / number.get(i);
                    }


                }

                String tr1 = Double.toString(result);
                tv.setText(tr1);
                /*try{
                    SharedPreferences sharedpreference = PreferenceManager.getDefaultSharedPreferences(this);
                    SharedPreferences.Editor editor = sharedpreference.edit();
                    editor.putString("result",tr1);
                    editor.commit();
                }catch(Exception e)
                {
                        Toast.makeText(this,"Error",Toast.LENGTH_LONG).show();
                }*/

                try{

                    file = new File(Environment.getExternalStorageDirectory(),"result.txt");
                    OutputStream fileOutput = new FileOutputStream(file);

                    OutputStreamWriter outputStreamWriter = new OutputStreamWriter(fileOutput);
                    outputStreamWriter.append(tr1);
                    outputStreamWriter.close();
                    fileOutput.flush();
                    fileOutput.close();

                }catch(Exception e)
                {
                    Toast.makeText(this,"Error",Toast.LENGTH_LONG).show();
                }
            }
            else
            {
                //result = Integer.parseInt(temp);
                //String tr = Double.toString(result);
                re = re+temp;
                int temppp = Integer.parseInt(re);
                result = temppp;
                tv.setText(re);
            }
        }
    }
}
