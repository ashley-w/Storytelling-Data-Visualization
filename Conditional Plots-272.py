## 2. Introduction to the Data Set ##

import pandas as pd
titanic = pd.read_csv('train.csv')
titanic = titanic[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
titanic = titanic.dropna()

## 3. Creating Histograms In Seaborn ##

# Import seaborn as sns
import seaborn as sns
# Import matplotlib
import matplotlib.pyplot as plt

# Visualize distribution of 'Age' column
sns.distplot(titanic['Age'])
# Display the plot
plt.show()

## 4. Generating A Kernel Density Plot ##

sns.kdeplot(titanic['Age'], shade=True)
plt.xlabel('Age')

## 5. Modifying The Appearance Of The Plots ##

# Set white background w/o grid
sns.set_style('white')

# Generate kernal density plot for age with shading\
sns.kdeplot(titanic['Age'], shade=True)
plt.xlabel('Age')

# Despine axes
sns.despine(left=True, bottom=True)


## 6. Conditional Distributions Using A Single Condition ##

g = sns.FacetGrid(titanic, col='Pclass', size=6)
g.map(sns.kdeplot, 'Age', shade=True)

sns.despine(left=True, bottom=True)
plt.show()

## 7. Creating Conditional Plots Using Two Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 8. Creating Conditional Plots Using Three Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue='Sex', size=3)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 9. Adding A Legend ##

g = sns.FacetGrid(titanic, col='Survived', row='Pclass', hue='Sex', size=3)
g.map(sns.kdeplot, 'Age', shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)

plt.show()