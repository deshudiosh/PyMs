# -*- mode: python -*-

import PyInstaller.config
PyInstaller.config.CONF['distpath'] = "."

# options = [ ('v', None, 'OPTION'), ('W ignore', None, 'OPTION') ]

a = Analysis(['pyms.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=None)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=None)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PyMs',
          debug=True,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
