#include<iostream>
#include<vector>

using namespace std;

int main()
{
	vector<int> data;
	int n;
	while (cin>>n) {
		data.push_back(n);
	}
	for (int i = 0; i < data.size(); i++) {
		if (data[i] != 42)
			cout<<data[i]<<endl;
		else
			break;
	}

	return 0;
}
