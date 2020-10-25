$(function(){
    //获取输入框元素
    var res=$('.result');
    //获取结果显示框
    var sum=$('.sum');
    var resval=0;
    var sumval=0;
    var operator=-1;
    var jon=['+','_','*','','%'];
    //求10的幂函数
    function funm(n){
        if(n==0){
            return 1
        }
        return funm(n-1)*10           		
    }     
   
    //AC清除按钮
    $('.dump').on('click',function(){
       res.val('0');
       resval=0;
       sum.val('');
       sumber=0;
       operator=-1;
    });
    //C清楚按钮
    $('.clear').on('click',function(){
        if(resval!='0'){
            resval=resval.slice(0,resval.length-1);
            res.val(resval);
        }
    })
    //数字按钮
    $(".number").on('click',function(){   
    //如果当前输入框数字为0或前一次输入为等号时 
       if(operator==0){
            operator=-1;
            res.val('0');
            resval=''; 
       } 
       if(resval=="0"){
            res.val('0');
            resval=''; 
       }
        
       resval=resval+$(this).html();
       res.val(resval);
    });
             
     //小数点
    $('.spot').on('click',function(){
        //遍历输入框数字，检查是否有小数点
         for(var i=0;i<resval.length;i++){
             if(resval[i]=="."){
                 return false;
             }
         }   
          if(operator==0){
            operator=1;
         res.val('0')
            resval=res.val(); 
       }   	 
              resval=resval+$(this).html();
             res.val(resval);        
    });
     //运算符
     $('.oper').on('click',function(){
         if(operator != 0){
         switch(operator){
            case 0:
                 resval=Number(sumval)+Number(resval);             	     
                 break;
            case 1:
                 resval=Number(sumval)+Number(resval);             	     
                 break;
            case 2:
                 resval=Number(sumval)-Number(resval);
                 break;
            case 3:
                 resval=Number(sumval)*Number(resval);
                 break;
            case 4:
                 resval=Number(sumval)/Number(resval);
                 break;
            case 5:
                 resval=Number(sumval)%Number(resval);
                 break;
        } 
         }
         operator=Number($(this).attr('operator'));
        sumval=resval;
        sum.val(resval+jon[operator-1]);
        resval=0;
        res.val('');
     })
     //等于
     $('.equal').on('click',function(){
         
        switch(operator){
            case 0:
                 sum.val(sumval+'+'+resval);
                 resval=Number(sumval)+Number(resval);             	     
                 res.val(resval);
                 operator=0;
                 break;
            case 1:
                 sum.val(sumval+'+'+resval);
                 resval=Number(sumval)+Number(resval);             	     
                 res.val(resval);
                 operator=0;
                 break;
            case 2:
                 sum.val(sumval+'-'+resval);
                 resval=Number(sumval)-Number(resval);
                 res.val(resval); 
                 operator=0;
                 break;
            case 3:
                 sum.val(sumval+'*'+resval);
                 resval=Number(sumval)*Number(resval);
                 res.val(resval);       
                 operator=0;
                 break;
            case 4:
                 sum.val(sumval+'/'+resval);
                 resval=Number(sumval)/Number(resval);
                 res.val(resval);
                 operator=0;
                 break;
            case 5:
                 sum.val(sumval+'%'+resval);
                 resval=Number(sumval)%Number(resval);
                 res.val(resval);
                 operator=0;
                 break;
        }
     });



});