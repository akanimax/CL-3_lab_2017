<%--
  Created by IntelliJ IDEA.
  User: botman
  Date: 5/4/17
  Time: 9:54 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Insert title here</title>
</head>
<body>
<%
    int i,j,temp;

    String nos=request.getParameter("nos");
    String[] s=nos.split(",");
    int[] a=new int[s.length];
    for( i=0;i<s.length;i++)
    {
        a[i]=Integer.parseInt(s[i]);
        //System.out.println(a.length);
    }

    for(int k=0;k<a.length;k++)  //pass
    {
        //even sort
        for(j=0;j<a.length-1;j++)
        {if(j%2==0)
        {
            if(a[j] > a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
        }


        //odd sort
        for(j=0;j<a.length-1;j++)
        {if(j%2!=0)
        {
            if(a[j] > a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
        }

    }
    for(i=0;i<a.length;i++)
    {

        out.println(a[i]);
    }
%>
</body>
</html>