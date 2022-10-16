// CPP program to do level order traversal
// of a generic tree
#include <iostream>
#include <string>
//#include <sstream>
//#include <bits/stdc++.h>
//#include <iomanip>      // std::setprecision
//#include <math.h> 
#include <vector>
#include<queue>

using namespace std;
  
// Represents a node of an n-ary tree
struct Node
{
    string key;
    vector<Node *> child;
};
  
 // Utility function to create a new tree node
Node *newNode(string key)
{
    Node *temp = new Node;
    temp->key = key;
    return temp;
}
 
// Print the n-ary tree level wise
void LevelOrderTraversal(Node * root)
{
    if (root==NULL)
        return;
  
    // Standard level order traversal code
    // using queue
    queue <Node *> q;  // Create a queue
    q.push(root); // Enqueue root
    while (!q.empty())
    {
        int n = q.size();
 
        // If this node has children
        while (n > 0)
        {
            // Dequeue an item from queue and prstring it
            Node * p = q.front();
            q.pop();
            cout << p->key << " "<<endl;
  
            // Enqueue all children of the dequeued item
            for (int i=0; i<p->child.size(); i++)
                q.push(p->child[i]);
            n--;
        }
  
        cout << endl; // Prstring new line between two levels
    }
}
  
// Driver program
int main()
{
    /*   Let us create below tree
    *              10
    *        /   /    \   \
    *        2  34    56   100
    *       / \         |   /  | \
    *      77  88       1   7  8  9
    */
    Node *root = newNode("University");
    (root->child).push_back(newNode("Name"));
    (root->child).push_back(newNode("Address"));
    (root->child[1]->child).push_back(newNode("Street_Name"));
    (root->child[1]->child).push_back(newNode("Area_Name"));
    (root->child[1]->child).push_back(newNode("City"));
    (root->child[1]->child).push_back(newNode("State"));
    (root->child[1]->child).push_back(newNode("Country"));
    (root->child).push_back(newNode("Vice_Chancellor"));
    (root->child[2]->child).push_back(newNode("Name"));
    (root->child[2]->child).push_back(newNode("Contact_Number"));
    (root->child[2]->child).push_back(newNode("EmailID"));
    (root->child[2]->child).push_back(newNode("Address"));
    (root->child[2]->child[3]->child).push_back(newNode("Street_Name"));
    (root->child[2]->child[3]->child).push_back(newNode("Area name"));
    (root->child[2]->child[3]->child).push_back(newNode("City"));
    (root->child[2]->child[3]->child).push_back(newNode("State"));
    (root->child[2]->child[3]->child).push_back(newNode("Country"));
    (root->child[2]->child).push_back(newNode("Dean1"));
    (root->child[2]->child[4]->child).push_back(newNode("Name of Faculty"));
    (root->child[2]->child[4]->child).push_back(newNode("Name"));
    (root->child[2]->child[4]->child).push_back(newNode("Contact number"));
    (root->child[2]->child[4]->child).push_back(newNode("Email ID"));
    (root->child[2]->child[4]->child).push_back(newNode("Address"));
    (root->child[2]->child[4]->child[4]->child).push_back(newNode("Street Name"));
    (root->child[2]->child[4]->child[4]->child).push_back(newNode("Area Name"));
    (root->child[2]->child[4]->child[4]->child).push_back(newNode("City"));
    (root->child[2]->child[4]->child[4]->child).push_back(newNode("State"));
    (root->child[2]->child[4]->child[4]->child).push_back(newNode("Country"));
  
    cout << "Level order traversal Before Mirroring\n";
    LevelOrderTraversal(root);
   
    return 0;
}