//
// Created by Iulia on 22.02.2021.
//
#include <stdio.h>

int print_menu()
{
    printf("\n1.Read an array\n");
    printf("2.Decompose a given natural number in its prime factors.\n");
    printf("3.Find the longest contiguous subsequence such that any consecutive elements contain the same digits.\n");
    printf("4.Find the longest contiguous subsequence such that any two consecutive elements have contrary signs.\n");
    printf("5.Exit\n");
    return 0;
}

int prime_nr(int n)
{
    /*function that checks whether a given nr is prime or not
     it returns 1 if it is or 0 otherwise */

    if (n<2)
        return 0;
    if (n==2)
        return 1;
    if (n%2==0)
        return 0;
    for (int i=3;i*i<=n;i=i+2)
        if (n%i==0)
            return 0;
    return 1;
}

int decompose_number(int nr,int v[])
{   /*function that decomposes a given nr in its prime factors
     we put the prime factors in a vector and we return its length*/

    int i=0;
    for (int d=2;d<=nr/2;d++)
        if (prime_nr(d)==1 && nr%d==0)
        {   int nr1=nr;
            while(nr1%d==0) {
                v[i] = d;
                i++;
                nr1=nr1/d;
            }
        }
    return i;

}

void print_decomposition(int n)
//function that prints the decomposition of the given nr
{   int v[1000];
    int nr_elem=decompose_number(n,v);
    if (nr_elem == 0)
        printf("The given number is prime");
    else {
        printf(" %d= ", n);
        for (int i = 0; i < nr_elem; i++)
        {
            if (i!=nr_elem-1)
                printf("%d*", v[i]);
            else
                printf("%d", v[i]);
        }

    }
    printf("\n");
}

void read_vector(int v[],int* n)
//function that reads a vector
{
    printf("Enter the dimension of the vector>>> ");
    scanf("%d", n);
    printf("Enter the elements of the vector>>>\n");
    for (int i=0;i<*n;i++)
    {
        scanf("%d", &v[i]);

    }

}

int have_same_digits(int a, int b)
//function that checks whether 2 nr have the same digits
//it returns 1 if they do or 0 otherwise
{   int fa[10]={0,0,0,0,0,0,0,0,0,0},fb[10]={0,0,0,0,0,0,0,0,0,0};
    if (a<0) a=-a;
    if(b<0) b=-b;
    while(a!=0)
    {
        fa[a%10]++;
        a=a/10;
    }
    while(b!=0)
    {
        fb[b%10]++;
        b=b/10;
    }
    for(int i=0;i<=9;i++)
        if((fa[i]==0 && fb[i]!=0 )||(fa[i]!=0 && fb[i]==0))
            return 0;
    return 1;
}

int have_contrary_signs(int a, int b)
//function which checks whether 2 numbers have opposite signs
{
    if (a*b<0)
        return 1;
    return 0;
}

void longest_seq_8b(int v[], int n, int indices[])
/* function to find the starting and ending point of the longest subsequence
 * that respects the given condition */
{
    int max_len=-1, i,current_len,position,start=0,end=0;
    for (i=0; i<n-1;i++)
    {   position=i;
        current_len=1;
        while (i<n-1 && have_contrary_signs(v[i], v[i+1])==1)
        {
            i++;
            current_len++;
        }
        if (current_len > max_len)
        {   max_len=current_len;
            start = position;
        }
    }
    end=start+max_len;
    indices[0]=start;
    indices[1]=end;

}

void longest_seq(int v[], int n, int indices[])
/* function to find the starting and ending point of the longest subsequence
 * that respects the given condition */
{
    int max_len=-1, i,current_len,position,start=0,end=0;
    for (i=0; i<n-1;i++)
    {   position=i;
        current_len=1;
        while (i<n-1 && have_same_digits(v[i], v[i+1])==1)
        {
            i++;
            current_len++;
        }
        if (current_len > max_len)
        {max_len=current_len;
         start = position;
        }
    }

    end=start+max_len;
    indices[0]=start;
    indices[1]=end;

}

void print_sequence(int v[],int start, int end)
//function to print the subsequence
{   int i;
    printf("The longest subsequence with the given property is: ");
    for (i=start;i<end;i++)
        printf("%d ", v[i]);
    printf("\n");
}


void start()
{
    print_menu();
    int ex,n=0, done=1,v[1000], ind[2],n1;
    while(done==1) {
        printf("Enter a command>>> ");
        scanf("%d", &ex);
        if (ex == 2) {
            printf("Enter the number you want to decompose>>> ");
            scanf("%d", &n1);
            print_decomposition(n1);

        } else {
            if (ex == 1)
                read_vector(v,&n);
            else {
                if (ex == 3) {
                    if (n==0)
                    {
                        printf("Please read the vector first!\n");
                    }
                    else {
                        longest_seq(v, n, ind);
                        print_sequence(v, ind[0], ind[1]);
                    }


                } else if (ex == 5) {done=0;
                    printf("Bye bye!");
                }
                else if (ex==4)
                {
                    if (n==0)
                    {
                        printf("Please read the vector first!\n");
                    }
                    else {
                        longest_seq_8b(v, n, ind);
                        print_sequence(v, ind[0], ind[1]);
                    }
                }
                else
                    printf("Bad command\n");

            }

        }
    }
}
int main()
{
    start();
    return 0;
}
