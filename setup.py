from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plonetheme.classic',
      version=version,
      description="An installable theme for Plone 3",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='web zope plone theme',
      author="''",
      author_email='product-developers@lists.plone.org',
      url='http://svn.plone.org/svn/plone/plonetheme.classic',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[],
      )
