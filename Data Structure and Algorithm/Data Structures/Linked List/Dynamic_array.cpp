#include<bits/stdc++.h>
#include<stdlib.h>
#include<conio.h>
using namespace std;
class DynamicArray
{
private:
    int capacity,lastIndex;
    int *arr;
public:
   void createArray(int cap){
        capacity=cap;
        arr=new int[capacity];
        lastIndex=-1;
    }
    void append_item(int data){
        if(lastIndex==capacity-1){
            doubleArray();
            lastIndex++;
            arr[lastIndex]=data;
        }
        else{
         arr[lastIndex+1]=data;
         lastIndex++;
        }
    }
    int get_item(int index){
        if(index<=lastIndex&&index>=0)
        return arr[index];
        else
            cout<<"OPERATION FAILED: INVALID INDEX!"<<endl;
    }
    int count_totalItems(){
        return lastIndex+1;
    }
    void view_all(){
        for(int i=0;i<=lastIndex;i++){
            cout<<arr[i]<<" ";
        }
            cout<<endl;
    }
    void insert_item(int index,int data){
        if(index<0||index>lastIndex+1){
            cout<<"OPERATION FAILED: INVALID INDEX!"<<endl;
        }
        else if(lastIndex==capacity-1){
            doubleArray();
            for(int i=lastIndex;i>=index;i--){
                arr[i+1]=arr[i];
            }
            arr[index]=data;
            lastIndex++;

        }
        else{
            for(int i=lastIndex;i>=index;i--){
                arr[i+1]=arr[i];
            }
            arr[index]=data;
            lastIndex++;
        }
    }
    void delete_item_atIndex(int index){
        if(index<0||index>lastIndex){
            cout<<"OPERATION FAILED: INVALID INDEX!"<<endl;
        }
        else{
            for(int i=index;i<lastIndex;i++){
                arr[i]=arr[i+1];
            }
            lastIndex--;
            if(lastIndex+1==capacity/2){
                halfArray();
            }
        }   
    }
    void edit_item_atIndex(int index,int data){
        if(index<0||index>lastIndex){
            cout<<"OPERATION FAILED: INVALID INDEX!"<<endl;
        }
        else{
            arr[index]=data;
        }
    }
    int search_item(int data){
        int i;
        for(i=0;i<=lastIndex;i++){
            if(arr[i]==data){
                return i;
            }
        }
        cout<<"DATA NOT FOUND"<<endl;
        return -1;
    }
    void doubleArray(){
        capacity=2*capacity;
        int *ptr=new int[capacity];
        for(int i=0;i<=lastIndex;i++){
            ptr[i]=arr[i];
        }
        delete []arr;
        arr=ptr;
    }
    void halfArray(){
        capacity=capacity/2;
        int *ptr=new int[capacity];
        for(int i=0;i<=lastIndex;i++)
        {
            ptr[i]=arr[i];
        }
        delete []arr;
        arr=ptr;
    }
    int getsize(){
        return capacity;
    }
};
int menu()
{
    int choice;
    cout<<"1.Append"<<endl;
    cout<<"2.Insert"<<endl;
    cout<<"3.Delete"<<endl;
    cout<<"4.Edit"<<endl;
    cout<<"5.Search"<<endl;
    cout<<"6.Size of DynamicArray"<<endl;
    cout<<"7.Exit"<<endl;
    cout<<"Enter your choice: "<<endl;
    cin>>choice;
    return choice;
}
void viewArrayData(DynamicArray &A){
    for(int i=0;i<A.count_totalItems();i++){
        cout<<A.get_item(i)<<" ";
    }
    cout<<endl;
}
int main(){
    int data,index;
    DynamicArray a;
    a.createArray(4);
    while(true){
       system("cls");
       cout<<"Total elements in Array: "<<a.count_totalItems()<<endl;
       viewArrayData(a);
       switch(menu()){
       case 1:
        cout<<"Enter data to Append:";
        cin>>data;
        a.append_item(data);
        break;
       case 2:
        cout<<"Enter data to Insert:";
        cin>>data;
        cout<<"Enter index to Insert:";
        cin>>index;
        a.insert_item(index,data);
        break;
       case 3:
        cout<<"Enter index to Delete:";
        cin>>index;
        a.delete_item_atIndex(index);
        break;
       case 4:
        cout<<"Enter data to Edit:";
        cin>>data;
        cout<<"Enter index to Edit:";
        cin>>index;
        a.edit_item_atIndex(index,data);
        break;
       case 5:
        cout<<"Enter data to Search:";
        cin>>data;
        index=a.search_item(data);
        if(index==-1){
            cout<<"OPERATION FAILED: DATA NOT FOUND!"<<endl;
        }
            else{
                cout<<"Element present at index: "<<index<<endl;
            }
        break;
       case 6:
        cout<<"size of DynamicArray is "<<a.getsize()<<endl;
        break;
       case 7:
        exit(0);
       default:
        cout<<"INVALID CHOICE!!"<<endl;
       }
       getch();
       
    return 0;
}